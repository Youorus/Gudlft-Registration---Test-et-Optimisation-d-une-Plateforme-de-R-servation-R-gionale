from server import loadCompetitions


def test_load_competitions():
    # Teste la fonction loadCompetitions() pour vérifier son bon fonctionnement.

    # Charge la liste des compétitions en appelant la fonction loadCompetitions()
    competitions = loadCompetitions()

    # Vérifie que la variable competitions est bien une liste
    assert isinstance(competitions, list)

    # Vérifie que la liste n'est pas vide, ce qui implique qu'il y a des compétitions chargées
    assert len(competitions) > 0

    # Vérifie que chaque compétition dans la liste contient les clés 'name', 'date' et 'numberOfPlaces'
    # Cela assure que les données des compétitions sont structurées correctement
    assert all(
        "name" in comp and "date" in comp and "numberOfPlaces" in comp
        for comp in competitions
    )
