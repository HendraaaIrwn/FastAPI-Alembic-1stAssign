from sqlmodel import Session, create_engine

engine = create_engine("sqlite:///database.db")

def get_db():
    with Session(bind=engine) as session:
        yield session

