def test_points_display(client):
    # Teste l'affichage des points
    response = client.get("/pointsDisplay")

    # Vérifie que la réponse est correcte (status code 200)
    assert response.status_code == 200

    # Vérifie que le titre "Club Points Display" est bien présent dans la réponse
    assert b"Club Points Display" in response.data

    # Vérifie que les noms des clubs attendus apparaissent sur la page
    assert b"Simply Lift" in response.data
    assert b"Iron Temple" in response.data
