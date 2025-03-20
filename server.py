import json
from flask import Flask, render_template, request, redirect, flash, url_for


# Fonction pour charger la liste des clubs depuis le fichier 'clubs.json'
def loadClubs():
    with open("clubs.json") as c:
        listOfClubs = json.load(c)[
            "clubs"
        ]  # Charge les données des clubs depuis le fichier JSON
        return listOfClubs  # Retourne la liste des clubs


# Fonction pour charger la liste des compétitions depuis le fichier 'competitions.json'
def loadCompetitions():
    with open("competitions.json") as comps:
        listOfCompetitions = json.load(comps)[
            "competitions"
        ]  # Charge les compétitions depuis le fichier JSON
        return listOfCompetitions  # Retourne la liste des compétitions


# Initialisation de l'application Flask
app = Flask(__name__)
app.secret_key = "something_special"  # Clé secrète pour les flash messages

# Charger les compétitions et les clubs au démarrage de l'application
competitions = loadCompetitions()
clubs = loadClubs()


# Route pour afficher la page d'accueil
@app.route("/")
def index():
    return render_template("index.html")  # Rend la page index.html


# Route pour afficher un résumé du club après la soumission d'un email
@app.route("/showSummary", methods=["POST"])
def showSummary():
    try:
        # Récupère l'email du formulaire
        email = request.form["email"]

        # Vérifie si l'email est vide
        if not email.strip():
            raise ValueError("Email cannot be empty. Please try again.")

        # Recherche le club associé à l'email
        club = next(club for club in clubs if club["email"] == email)

        # Rend la page de bienvenue avec les informations du club et des compétitions
        return render_template("welcome.html", club=club, competitions=competitions)

    except StopIteration:
        # Si aucun club n'est trouvé avec cet email, afficher un message d'erreur
        flash("Email not found. Please try again.")
        return redirect(url_for("index"))  # Redirige vers la page d'accueil
    except KeyError:
        # Si les données envoyées ne sont pas valides, afficher un message d'erreur
        flash("Invalid form submission. Please try again.")
        return redirect(url_for("index"))
    except ValueError as e:
        # Si l'email est vide ou invalide, afficher un message d'erreur
        flash(str(e))
        return redirect(url_for("index"))
    except Exception as e:
        # Gérer toute autre exception
        flash(f"An unexpected error occurred: {str(e)}")
        return redirect(url_for("index"))


# Route pour afficher la page de réservation d'un club et d'une compétition
@app.route("/book/<competition>/<club>")
def book(competition, club):
    try:
        # Recherche le club et la compétition à partir des paramètres de l'URL
        foundClub = next(c for c in clubs if c["name"] == club)
        foundCompetition = next(c for c in competitions if c["name"] == competition)

        # Rend la page de réservation avec les informations du club et de la compétition
        return render_template(
            "booking.html", club=foundClub, competition=foundCompetition
        )

    except StopIteration:
        # Si aucun club ou compétition n'est trouvé, afficher un message d'erreur
        flash("Competition or club not found. Please try again.")
        return redirect(url_for("index"))  # Redirige vers la page d'accueil


# Route pour traiter la réservation de places pour une compétition
@app.route("/purchasePlaces", methods=["POST"])
def purchasePlaces():
    try:
        # Récupère les données du formulaire de réservation
        competition = next(
            c for c in competitions if c["name"] == request.form["competition"]
        )
        club = next(c for c in clubs if c["name"] == request.form["club"])
        places_required = int(request.form["places"])

        # Vérifier les contraintes de réservation
        if places_required <= 0:
            raise ValueError(
                "Invalid number of places. Please enter a positive number."
            )
        if places_required > int(club["points"]):
            raise ValueError("You do not have enough points to make this booking.")
        if places_required > 12:
            raise ValueError("You cannot book more than 12 places in a competition.")
        if places_required > int(competition["numberOfPlaces"]):
            raise ValueError("Not enough places available in this competition.")

        # Mettre à jour les points du club et le nombre de places disponibles dans la compétition
        club["points"] = int(club["points"]) - places_required
        competition["numberOfPlaces"] = (
            int(competition["numberOfPlaces"]) - places_required
        )

        # Afficher un message de confirmation après la réservation
        flash(f"Great-booking complete! {places_required} places booked.")
        return render_template("welcome.html", club=club, competitions=competitions)

    except (ValueError, StopIteration) as e:
        # Gérer les erreurs de valeur ou si le club/compétition n'est pas trouvé
        flash(str(e))
        return redirect(
            url_for(
                "book",
                competition=request.form["competition"],
                club=request.form["club"],
            )
        )


# Route pour afficher les points disponibles des clubs
@app.route("/pointsDisplay")
def pointsDisplay():
    return render_template(
        "points.html", clubs=clubs
    )  # Affiche les points de tous les clubs


# Route pour se déconnecter (redirige vers la page d'accueil)
@app.route("/logout")
def logout():
    return redirect(url_for("index"))  # Redirige vers la page d'accueil
