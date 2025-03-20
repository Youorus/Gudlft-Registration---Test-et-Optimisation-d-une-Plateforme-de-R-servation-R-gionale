def test_index(client):
    # Teste si la route '/' renvoie une réponse valide
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data