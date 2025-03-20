def test_points_display(client):
    # Teste l'affichage des points
    response = client.get('/pointsDisplay')
    assert response.status_code == 200
    assert b"Club Points Display" in response.data
    assert b"Simply Lift" in response.data
    assert b"Iron Temple" in response.data