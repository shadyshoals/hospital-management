import pytest
from app.schemas.user import AdminCreate
import random

def test_create_admin(client):
    admin_data = {
        "username": "admin_test",
        "first_name": "Buggsy",
        "last_name": "Malone",
        "department": "toilet",
        "permission_level": 0
    }
    for i in range(100):
        admin_data["username"] = "admin" + str(random.randint(0,100000))
        response = client.post("/users/admin", json=admin_data)
        assert response.status_code == 200
        data = response.json()
        # assert data["username"] == "admin_test"
        assert data["role"] == "admin"

def test_delete_admin(client):
    admin_data = {
        "username": "current_username",
        "first_name": "Buggsy",
        "last_name": "Malone",
        "department": "toilet",
        "permission_level": 0
    }
    client.post("/users/admin", json=admin_data)

    assert client.delete("/users/0").status_code == 204