


from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_user():
    response = client.post(
        "/register",
        json={"username": "testuser", "password": "testpassword"}
    )
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_register_duplicate_user():
    client.post(
        "/register",
        json={"username": "duplicateuser", "password": "testpassword"}
    )
    response = client.post(
        "/register",
        json={"username": "duplicateuser", "password": "testpassword"}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Username already exists"
