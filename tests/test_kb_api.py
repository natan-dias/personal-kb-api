# tests/test_main.py
import pytest

# Small workaround to use absolute imports
import sys
from pathlib import Path # if you haven't already done so
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

# Additionally remove the current file's directory from sys.path
try:
    sys.path.remove(str(parent))
except ValueError: # Already removed
    pass

from kb_api import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    yield app.test_client()
    #db.session.remove()
    #db.drop_all()

def test_healthcheck(client):
    response = client.get('/healthcheck')
    assert response.status_code == 200

def test_category_post(client):
    # Test posting a new category
    data = {'category': 'Test Category'}
    response = client.post('/categories', json=data)
    assert response.status_code == 201

def test_command_post(client):
    # Test posting a new command
    data = {'command': 'Test Command', 'command_description': 'Test description'}
    response = client.post('/categories/1/commands', json=data)
    assert response.status_code == 201