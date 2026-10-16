import pytest
from tasklist.app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_index_status_code_and_tasks(client):
    response = client.get("/")
    assert response.status_code == 200
    html = response.text
    assert "Buy groceries" in html
    assert "Pay electricity bill" in html
    assert "Schedule dentist appointment" in html
    assert "Water the plants" in html
    assert "Read a new book" in html

def test_invalid_timezone_fallback(client):
    response = client.get("/?tz=Mars/Base")
    assert response.status_code == 200
    assert "Today in UTC" in response.text
