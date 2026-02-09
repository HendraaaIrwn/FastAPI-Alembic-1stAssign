from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.models.database import Trains
from app.models.engine import get_db
from app.schema.trains import TrainsRequestSchema, TrainsResponseSchema

trains_router = APIRouter(tags=["Trains"])


@trains_router.get("/trains", response_model=list[TrainsResponseSchema])
def get_trains(db: Session = Depends(get_db)):
    stmt = select(Trains)
    result = db.exec(stmt)
    trains = result.all()
    return trains

@trains_router.get("/trains/{train_id}", response_model=TrainsResponseSchema)
def get_train_by_id(train_id: UUID, db: Session = Depends(get_db)):
    train = db.get(Trains, train_id)
    if train is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Train not found",
        )
    return train

@trains_router.get("/trains/origin/{origin}/destination/{destination}", response_model=list[TrainsResponseSchema])
def get_trains_by_route(origin: str, destination: str, db: Session = Depends(get_db)):
    stmt = select(Trains).where(Trains.origin == origin, Trains.destination == destination)
    result = db.exec(stmt)
    trains = result.all()
    return trains   

@trains_router.post("/trains", response_model=TrainsResponseSchema)
def create_train(train: TrainsRequestSchema, db: Session = Depends(get_db)):
    db_train = Trains(**train.model_dump())
    db.add(db_train)
    db.commit()
    db.refresh(db_train)
    return db_train

@trains_router.put("/trains/{train_id}", response_model=TrainsResponseSchema)
def update_train(train_id: UUID, updated_train: TrainsRequestSchema, db: Session = Depends(get_db)):
    train = db.get(Trains, train_id)
    if train is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Train not found",
        )

    train.train_name = updated_train.train_name
    train.price = updated_train.price
    train.origin = updated_train.origin
    train.destination = updated_train.destination
    train.departure_time = updated_train.departure_time
    train.arrival_time = updated_train.arrival_time
    db.add(train)
    db.commit()
    db.refresh(train)
    return train

@trains_router.delete("/trains/{train_id}")
def delete_train(train_id: UUID, db: Session = Depends(get_db)):
    train = db.get(Trains, train_id)
    if train is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Train not found",
        )
    db.delete(train)
    db.commit()
    return {"message": "Train deleted successfully"}    
