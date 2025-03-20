
from server import loadCompetitions

def test_load_competitions():
    competitions = loadCompetitions()
    assert isinstance(competitions, list)
    assert len(competitions) > 0
    assert all("name" in comp and "date" in comp and "numberOfPlaces" in comp for comp in competitions)