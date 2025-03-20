def test_show_summary_valid_email(client):
    # Teste un email valide
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
    assert response.status_code == 200
    assert b"Welcome, john@simplylift.co" in response.data

def test_show_summary_invalid_email(client):
    # Teste un email invalide
    response = client.post('/showSummary', data={'email': 'invalid@example.com'}, follow_redirects=True)
    assert response.status_code == 200  # La redirection a été suivie
    assert b"Email not found" in response.data  # Vérifie le message flash

def test_show_summary_empty_email(client):
    # Teste un email vide
    response = client.post('/showSummary', data={'email': ''}, follow_redirects=True)
    assert response.status_code == 200  # La redirection a été suivie
    assert b"Email cannot be empty" in response.data  # Vérifie le message flash