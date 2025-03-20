# tests/unit/test_load_clubs.py
from server import loadClubs

def test_load_clubs():
    clubs = loadClubs()
    assert isinstance(clubs, list)
    assert len(clubs) > 0
    assert all("name" in club and "email" in club and "points" in club for club in clubs)