import uuid
from pydantic import BaseModel, ConfigDict


class PassengersResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    passenger_name: str
    email: str
    phone_number: str
    seat_number: int
    train_id: uuid.UUID

class PassengersRequestSchema(BaseModel):
    passenger_name: str
    email: str
    phone_number: str
    seat_number: int
    train_id: uuid.UUID
