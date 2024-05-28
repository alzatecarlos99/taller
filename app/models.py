from pydantic import BaseModel
from typing import Optional


class SOAT(BaseModel):
    company_name: str
    start_date: str
    end_date: str


class Vehicle(BaseModel):
    license_plate: str
    brand: str
    model: str
    soat: Optional[SOAT] = None
