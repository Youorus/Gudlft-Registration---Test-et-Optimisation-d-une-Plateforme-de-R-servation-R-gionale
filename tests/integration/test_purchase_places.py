def test_purchase_places_valid(client):
    # Teste une réservation valide
    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Simply Lift',
        'places': '5'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Great-booking complete!" in response.data

def test_purchase_places_invalid_points(client):
    # Teste une réservation avec des points insuffisants
    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Simply Lift',
        'places': '20'
    }, follow_redirects=True)
    assert response.status_code == 200  # La redirection a été suivie
    assert b"You do not have enough points" in response.data  # Vérifie le message flash

def test_purchase_places_invalid_places(client):
    # Teste une réservation avec un nombre de places invalide
    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Simply Lift',
        'places': '-5'
    }, follow_redirects=True)
    assert response.status_code == 200  # La redirection a été suivie
    assert b"Invalid number of places" in response.data  # Vérifie le message flash