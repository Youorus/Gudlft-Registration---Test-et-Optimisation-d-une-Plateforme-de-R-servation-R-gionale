def test_logout(client):
    # Teste la déconnexion
    response = client.get("/logout")

    # Vérifie que la redirection se fait correctement vers la page d'accueil (index)
    assert response.status_code == 302  # Le code 302 indique une redirection
    assert (
        response.headers["Location"] == "/"
    )  # Vérifie que l'utilisateur est redirigé vers l'index
