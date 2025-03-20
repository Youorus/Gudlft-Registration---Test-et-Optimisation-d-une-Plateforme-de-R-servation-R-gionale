import pytest
import sys
import os

# Ajouter le répertoire parent au PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from server import app as flask_app

@pytest.fixture
def app():
    # Configuration de l'application Flask pour les tests
    flask_app.config.update({
        "TESTING": True,
    })
    yield flask_app

@pytest.fixture
def client(app):
    # Crée un client de test pour simuler des requêtes HTTP
    return app.test_client()

@pytest.fixture
def runner(app):
    # Crée un runner pour exécuter des commandes CLI
    return app.test_cli_runner()