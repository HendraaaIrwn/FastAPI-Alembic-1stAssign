import uuid
from pydantic import BaseModel, ConfigDict


class TrainsRequestSchema(BaseModel):
    train_name: str
    price: int
    origin: str
    destination: str
    departure_time: str
    arrival_time: str


class TrainsResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    train_name: str
    price: int
    origin: str
    destination: str
    departure_time: str
    arrival_time: str
