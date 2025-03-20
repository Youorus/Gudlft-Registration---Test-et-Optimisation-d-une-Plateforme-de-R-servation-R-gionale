def test_book_valid_competition_and_club(client):
    # Teste une compétition et un club valides
    # Envoie une requête GET pour réserver une place pour la compétition "Spring Festival" pour le club "Simply Lift"
    response = client.get("/book/Spring Festival/Simply Lift")

    # Vérifie que la réponse HTTP a un code de statut 200 (OK), indiquant que la page de réservation a été rendue correctement
    assert response.status_code == 200

    # Vérifie que le texte "Booking for Spring Festival" est présent dans la réponse
    # Cela confirme que la page de réservation pour cette compétition a bien été affichée
    assert b"Booking for Spring Festival" in response.data


def test_book_invalid_competition(client):
    # Teste une compétition invalide
    # Envoie une requête GET pour réserver une place pour une compétition invalide "Invalid Competition" pour le club "Simply Lift"
    response = client.get(
        "/book/Invalid Competition/Simply Lift", follow_redirects=True
    )

    # Vérifie que la réponse HTTP a un code de statut 200 après redirection
    # La redirection vers une autre page est suivie, donc le code de statut attendu est 200
    assert response.status_code == 200

    # Vérifie que le message "Competition or club not found" est présent dans la réponse
    # Cela confirme que le système a détecté que la compétition n'est pas valide et affiche le message d'erreur approprié
    assert (
        b"Competition or club not found" in response.data
    )  # Vérification du message flash


def test_book_invalid_club(client):
    # Teste un club invalide
    # Envoie une requête GET pour réserver une place pour la compétition "Spring Festival" pour un club invalide "Invalid Club"
    response = client.get("/book/Spring Festival/Invalid Club", follow_redirects=True)

    # Vérifie que la réponse HTTP a un code de statut 200 après redirection
    # La redirection vers une autre page est suivie, donc le code de statut attendu est 200
    assert response.status_code == 200

    # Vérifie que le message "Competition or club not found" est présent dans la réponse
    # Cela confirme que le système a détecté que le club n'est pas valide et affiche le message d'erreur approprié
    assert (
        b"Competition or club not found" in response.data
    )  # Vérification du message flash
