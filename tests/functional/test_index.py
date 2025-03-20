def test_index(client):
    # Teste si la route '/' renvoie une réponse valide
    # Envoie une requête GET à la page d'accueil (route "/")
    response = client.get("/")

    # Vérifie que la réponse HTTP a un code de statut 200 (OK), ce qui signifie que la page a été rendue correctement
    assert response.status_code == 200

    # Vérifie que le texte "Welcome to the GUDLFT Registration Portal!" est présent dans la réponse
    # Cela confirme que la page d'accueil contient bien le message attendu, indiquant que la page d'accueil fonctionne comme prévu
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data
