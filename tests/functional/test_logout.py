def test_logout(client):
    # Teste la déconnexion
    response = client.get('/logout')
    assert response.status_code == 302  # Redirection vers l'index