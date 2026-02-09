from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from uuid import UUID
from app.models.database import Passengers
from app.models.engine import get_db
from app.schema.passengers import PassengersRequestSchema, PassengersResponseSchema



passenger_router = APIRouter(tags=["Passengers"])

@passenger_router.get("/passengers", response_model=list[PassengersResponseSchema])
def get_passengers(db: Session = Depends(get_db)):
    stmt = select(Passengers)
    result = db.exec(stmt)
    passengers = result.all()
    return passengers
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Train not found",
        )
    db.delete(train)
    db.commit()
    return passengers   

@passenger_router.get("/passengers/{passenger_id}", response_model=PassengersResponseSchema)
def get_passenger_by_id(passenger_id: UUID, db: Session = Depends(get_db)):
    passenger = db.get(Passengers, passenger_id)
    if passenger is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Passenger not found",
        )
    return passenger    

@passenger_router.post("/passengers", response_model=PassengersResponseSchema)
def create_passenger(passenger: PassengersRequestSchema, db: Session = Depends(get_db)):
    db_passenger = Passengers(**passenger.model_dump())
    db.add(db_passenger)
    db.commit()
    db.refresh(db_passenger)
    return db_passenger 

@passenger_router.put("/passengers/{passenger_id}", response_model=PassengersResponseSchema)
def update_passenger(passenger_id: UUID, updated_passenger: PassengersRequestSchema, db: Session = Depends(get_db)):
    passenger = db.get(Passengers, passenger_id)
    if passenger is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Passenger not found",
        )

    passenger.passenger_name = updated_passenger.passenger_name
    passenger.email = updated_passenger.email
    passenger.phone_number = updated_passenger.phone_number
    db.add(passenger)
    db.commit()
    db.refresh(passenger)
    return passenger    

@passenger_router.delete("/passengers/{passenger_id}")
def delete_passenger(passenger_id: UUID, db: Session = Depends(get_db)):
    passenger = db.get(Passengers, passenger_id)
    if passenger is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Passenger not found",
        )
    db.delete(passenger)
    db.commit()
    return {"detail": "Passenger deleted successfully"} 