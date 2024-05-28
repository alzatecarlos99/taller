# test_controller.py
import pytest
from .controller import create_vehicle, get_vehicles, update_vehicle, delete_vehicle, get_vehicle_by_plate
from .models import Vehicle

@pytest.fixture
def sample_vehicle():
    return Vehicle(
        license_plate="ABC123",
        brand="Toyota",
        model="Corolla",
        soat=None
    )

def test_create_vehicle(sample_vehicle):
    result = create_vehicle(sample_vehicle)
    assert result["license_plate"] == sample_vehicle.license_plate

def test_get_vehicles():
    result = get_vehicles()
    assert isinstance(result, list)

def test_update_vehicle(sample_vehicle):
    updated_vehicle = sample_vehicle
    updated_vehicle.model = "Camry"
    result = update_vehicle(sample_vehicle.license_plate, updated_vehicle)
    assert result["model"] == "Camry"

def test_delete_vehicle(sample_vehicle):
    result = delete_vehicle(sample_vehicle.license_plate)
    assert result["message"] == "Vehicle deleted"

def test_get_vehicle_by_plate(sample_vehicle):
    result = get_vehicle_by_plate(sample_vehicle.license_plate)
    assert result["license_plate"] == sample_vehicle.license_plate


# test_integration.py
from fastapi.testclient import TestClient
from .main import app
from .models import Vehicle

client = TestClient(app)

def test_add_vehicle():
    vehicle = {
        "license_plate": "XYZ789",
        "brand": "Honda",
        "model": "Civic",
        "soat": {
            "company_name": "InsuranceCo",
            "start_date": "2023-01-01",
            "end_date": "2024-01-01"
        }
    }
    response = client.post("/vehicles/", json=vehicle)
    assert response.status_code == 200
    assert response.json()["license_plate"] == "XYZ789"

def test_list_vehicles():
    response = client.get("/vehicles/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_vehicle():
    response = client.get("/vehicles/XYZ789")
    assert response.status_code == 200
    assert response.json()["license_plate"] == "XYZ789"

def test_modify_vehicle():
    vehicle = {
        "license_plate": "XYZ789",
        "brand": "Honda",
        "model": "Accord",
        "soat": {
            "company_name": "InsuranceCo",
            "start_date": "2023-01-01",
            "end_date": "2024-01-01"
        }
    }
    response = client.put("/vehicles/XYZ789", json=vehicle)
    assert response.status_code == 200
    assert response.json()["model"] == "Accord"

def test_remove_vehicle():
    response = client.delete("/vehicles/XYZ789")
    assert response.status_code == 200
    assert response.json()["message"] == "Vehicle deleted"