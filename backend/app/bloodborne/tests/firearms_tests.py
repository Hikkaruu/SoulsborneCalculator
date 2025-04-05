import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from ...main import app  
from ...database import Base, engine, SessionLocal, get_db

@pytest.fixture
def client():
    def override_get_db():
        try:
            db = SessionLocal()
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()

@pytest.fixture(autouse=True)
def prepare_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

# Test data
@pytest.fixture
def sample_firearm_data():
    return {
        "upgrade_lvl": 0,
        "name": "Test Pistol",
        "physical_atk": 100,
        "blood_atk": 50,
        "arcane_atk": 0,
        "fire_atk": 0,
        "bolt_atk": 0,
        "bullet_use": 1,
        "strength_scaling": 0.5,
        "skill_scaling": 0.8,
        "bloodtinge_scaling": 1.2,
        "arcane_scaling": 0,
        "socket": 0,
        "strenght_req": 6,
        "skill_req": 5,
        "bloodtinge_req": 8,
        "arcane_req": 0
    }


    return {
        "upgrade_lvl": 0,
        "name": "Test Pistol2",
        "physical_atk": 100,
        "blood_atk": 50,
        "arcane_atk": 0,
        "fire_atk": 0,
        "bolt_atk": 0,
        "bullet_use": 1,
        "strength_scaling": 0.5,
        "skill_scaling": 0.8,
        "bloodtinge_scaling": 1.2,
        "arcane_scaling": 0,
        "socket": 0,
        "strenght_req": 6,
        "skill_req": 5,
        "bloodtinge_req": 8,
        "arcane_req": 0
    }

# Tests
def test_get_firearm_by_id(client: TestClient):
    response = client.get(f"/firearms/id/23")
    assert response.status_code == 200
    assert response.json()["name"] == "Evelyn"

def test_create_firearm_valid(client: TestClient, sample_firearm_data):
    response = client.post("/firearms/", json=sample_firearm_data)
    assert response.status_code == 200

    data = response.json()
    
    for field in sample_firearm_data:
        assert field in data
        assert data[field] == sample_firearm_data[field]

    assert "id" in data 

def test_create_firearm_duplicate(client: TestClient, sample_firearm_data):
    client.post("/firearms/", json=sample_firearm_data)
    response = client.post("/firearms/", json=sample_firearm_data)
    assert response.status_code == 409

def test_create_firearm_negative_upgrade_lvl(client: TestClient, sample_firearm_data):
    modified_data = sample_firearm_data.copy()
    modified_data["upgrade_lvl"] = -1
    response = client.post("/firearms/", json=modified_data)
    assert response.status_code == 409

    

