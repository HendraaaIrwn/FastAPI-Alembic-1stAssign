import uuid
from sqlmodel import SQLModel, Relationship, Field

class Trains(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    train_name: str = Field(default="Train...")
    price: int = Field(default=0)
    origin: str = Field(default="Origin...")
    destination: str = Field(default="Destination...")
    departure_time: str = Field(default="00:00")
    arrival_time: str = Field(default="00:00")
    passengers: list["Passengers"] = Relationship(back_populates="train")
    
   
class Passengers(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    passenger_name: str = Field(default="Passenger...")
    email: str = Field(default="")
    phone_number: str = Field(default="")
    seat_number: int = Field(default=0)
    train_id: uuid.UUID = Field(foreign_key="trains.id")
    train: Trains = Relationship(back_populates="passengers")
