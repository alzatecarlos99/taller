from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from .models import Vehicle
from .controller import create_vehicle, get_vehicles, update_vehicle, delete_vehicle, get_vehicle_by_plate
import os

app = FastAPI()

@app.post("/vehicles/")
def add_vehicle(vehicle: Vehicle):
    return create_vehicle(vehicle)

@app.get("/vehicles/")
def list_vehicles():
    return get_vehicles()

@app.get("/vehicles/{license_plate}")
def get_vehicle(license_plate: str):
    return get_vehicle_by_plate(license_plate)

@app.put("/vehicles/{license_plate}")
def modify_vehicle(license_plate: str, vehicle: Vehicle):
    return update_vehicle(license_plate, vehicle)

@app.delete("/vehicles/{license_plate}")
def remove_vehicle(license_plate: str):
    return delete_vehicle(license_plate)

@app.get("/")
def read_root():
    return FileResponse(os.path.join('app', 'index.html'))