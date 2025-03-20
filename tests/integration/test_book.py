def test_book_valid_competition_and_club(client):
    # Teste une compétition et un club valides
    response = client.get('/book/Spring Festival/Simply Lift')
    assert response.status_code == 200
    assert b"Booking for Spring Festival" in response.data

def test_book_invalid_competition(client):
    # Teste une compétition invalide
    response = client.get('/book/Invalid Competition/Simply Lift', follow_redirects=True)
    assert response.status_code == 200  # La redirection a été suivie
    assert b"Competition or club not found" in response.data  # Vérifie le message flash

def test_book_invalid_club(client):
    # Teste un club invalide
    response = client.get('/book/Spring Festival/Invalid Club', follow_redirects=True)
    assert response.status_code == 200  # La redirection a été suivie
    assert b"Competition or club not found" in response.data  # Vérifie le message flash