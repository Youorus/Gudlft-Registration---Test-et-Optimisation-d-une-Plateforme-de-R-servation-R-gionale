def test_show_summary_valid_email(client):
    # Teste un email valide
    # Envoie une requête POST avec un email valide à l'URL "/showSummary"
    response = client.post("/showSummary", data={"email": "john@simplylift.co"})

    # Vérifie que la réponse HTTP a un code de statut 200 (OK), indiquant que la page a été correctement rendue
    assert response.status_code == 200

    # Vérifie que le message de bienvenue contenant l'email est présent dans la réponse
    assert b"Welcome, john@simplylift.co" in response.data


def test_show_summary_invalid_email(client):
    # Teste un email invalide
    # Envoie une requête POST avec un email invalide à l'URL "/showSummary"
    response = client.post(
        "/showSummary", data={"email": "invalid@example.com"}, follow_redirects=True
    )

    # Vérifie que la réponse HTTP a un code de statut 200 après redirection
    # La redirection vers une autre page est suivie, donc le code de statut attendu est 200
    assert response.status_code == 200

    # Vérifie que le message "Email not found" est présent dans la réponse
    # Cela confirme que le système a bien détecté que l'email n'est pas dans la base de données
    assert b"Email not found" in response.data  # Vérification du message flash


def test_show_summary_empty_email(client):
    # Teste un email vide
    # Envoie une requête POST avec un champ email vide à l'URL "/showSummary"
    response = client.post("/showSummary", data={"email": ""}, follow_redirects=True)

    # Vérifie que la réponse HTTP a un code de statut 200 après redirection
    # Le formulaire est redirigé après l'échec de la validation, donc le code de statut attendu est 200
    assert response.status_code == 200

    # Vérifie que le message "Email cannot be empty" est présent dans la réponse
    # Cela confirme que le système a correctement géré l'erreur d'email vide
    assert b"Email cannot be empty" in response.data  # Vérification du message flash
