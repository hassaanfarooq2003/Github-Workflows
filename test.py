import pytest
from app import app

@pytest.fixture
def client():
    app.testing=True
    with app.test_client() as client:
        yield client

def test_add(client):
    response = client.get('/add?a=1&b=2')
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data['result'] == 3

def test_subtract(client):
    response = client.get('/subtract?a=5&b=3')
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data['result'] == 2

def test_multiply(client):
    response = client.get('/multiply?a=2&b=3')
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data['result'] == 6

def test_divide(client):
    response = client.get('/divide?a=6&b=3')
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data['result'] == 2

def test_divide_by_zero(client):
    response = client.get('/divide?a=6&b=0')
    json_data = response.get_json()
    assert response.status_code == 400
    assert 'error' in json_data

def test_exponentiation(client):
    response = client.get('/exponent?a=2&b=3')
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data['result'] == 8

def test_sqrt(client):
    response = client.get('/sqrt?a=4')
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data['result'] == 2

def test_history(client):
    client.get('/add?a=1&b=2')
    client.get('/subtract?a=5&b=3')
    response = client.get('/history')
    json_data = response.get_json()
    assert response.status_code == 200
    assert len(json_data) >= 2