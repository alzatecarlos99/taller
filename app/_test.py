from .controller import create_vehicle, get_vehicles, update_vehicle, delete_vehicle, get_vehicle_by_plate
from .models import Vehicle
from fastapi.testclient import TestClient
from .main import app
from fastapi import HTTPException
import pytest

client = TestClient(app)

########### PRUEBAS UNITARIAS ######################


@pytest.mark.skip
def test_should_create_vehicle_when_calling_create_vehicle():
    # Arrange
    vehicle = Vehicle(license_plate="ABC123", brand="Toyota", model="Corolla", soat=None)
    # Act
    result = create_vehicle(vehicle)
    # Assert
    assert result["license_plate"] == "ABC123", "Expected the license plate to match the input"


@pytest.mark.skip
def test_should_list_vehicles_when_calling_get_vehicles():
    # Act
    result = get_vehicles()
    # Assert
    assert isinstance(result, list), "Expected result to be a list of vehicles"


@pytest.mark.skip
def test_should_update_vehicle_when_calling_update_vehicle():
    # Arrange
    vehicle = Vehicle(license_plate="ABC123", brand="Toyota", model="Corolla", soat=None)
    vehicle.model = "Camry"
    # Act
    result = update_vehicle("ABC123", vehicle)
    # Assert
    assert result["model"] == "Camry", "Expected the model to be updated to 'Camry'"


@pytest.mark.skip
def test_should_delete_vehicle_when_calling_delete_vehicle():
    # Act
    result = delete_vehicle("ABC123")
    # Assert
    assert result["message"] == "Vehicle deleted", "Expected confirmation message 'Vehicle deleted'"


@pytest.mark.skip
def test_should_get_vehicle_by_plate_when_calling_get_vehicle_by_plate():
    # Act
    with pytest.raises(HTTPException) as excinfo:
        get_vehicle_by_plate("ABC123")
    assert excinfo.value.status_code == 404, "Expected HTTP 404 for vehicle not found"


########### PRUEBAS DE INTEGRACION ############


@pytest.mark.skip
def test_integration_should_add_vehicle():
    # Arrange
    vehicle = {
        "license_plate": "XYZ789",
        "brand": "Honda",
        "model": "Civic",
        "soat": {"company_name": "InsuranceCo", "start_date": "2023-01-01", "end_date": "2024-01-01"},
    }
    # Act
    response = client.post("/vehicles/", json=vehicle)
    # Assert
    assert response.status_code == 200, "Expected status code 200"
    assert response.json()["license_plate"] == "XYZ789", "Expected to return the added vehicle license plate"
