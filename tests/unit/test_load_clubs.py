from server import loadClubs


def test_load_clubs():
    # Teste la fonction loadClubs() pour vérifier son bon fonctionnement.

    # Charge la liste des clubs en appelant la fonction loadClubs()
    clubs = loadClubs()

    # Vérifie que la variable clubs est bien une liste
    assert isinstance(clubs, list)

    # Vérifie que la liste n'est pas vide, ce qui implique qu'il y a des clubs chargés
    assert len(clubs) > 0

    # Vérifie que chaque club dans la liste contient les clés 'name', 'email' et 'points'
    # Cela assure que les données des clubs sont structurées correctement
    assert all(
        "name" in club and "email" in club and "points" in club for club in clubs
    )
