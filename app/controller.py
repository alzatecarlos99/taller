from pymongo import MongoClient
from .models import Vehicle
from bson import ObjectId
from fastapi import HTTPException

client = MongoClient("mongodb://localhost:27017/")
db = client["Taller"]
vehicle_collection = db["vehiculos"]

def create_vehicle(vehicle_data: Vehicle):
    try:
        vehicle_dict = vehicle_data.dict()
        result = vehicle_collection.insert_one(vehicle_dict)
        vehicle_dict["_id"] = str(result.inserted_id)
        return vehicle_dict
    except Exception as e:
        print(f"Error inserting vehicle: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

def get_vehicles():
    try:
        vehicles = list(vehicle_collection.find({}, {"_id": 0}))
        return vehicles
    except Exception as e:
        print(f"Error fetching vehicles: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

def update_vehicle(license_plate, vehicle_data: Vehicle):
    try:
        print(f"Updating vehicle with license_plate {license_plate} to: {vehicle_data.dict()}")
        vehicle_collection.update_one({"license_plate": license_plate}, {"$set": vehicle_data.dict()})
        return vehicle_data.dict()
    except Exception as e:
        print(f"Error updating vehicle: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

def delete_vehicle(license_plate):
    try:
        print(f"Deleting vehicle with license_plate: {license_plate}")
        vehicle_collection.delete_one({"license_plate": license_plate})
        return {"message": "Vehicle deleted"}
    except Exception as e:
        print(f"Error deleting vehicle: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
def get_vehicle_by_plate(license_plate: str):
    try:
        vehicle = vehicle_collection.find_one({"license_plate": license_plate}, {"_id": 0})
        if vehicle:
            return vehicle
        else:
            raise HTTPException(status_code=404, detail="Vehicle not found")
    except Exception as e:
        print(f"Error fetching vehicle by plate: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")