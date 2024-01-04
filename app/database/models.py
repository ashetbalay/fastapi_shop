from database import Base, engine
from sqlalchemy import Column, Integer, String


class Films(Base):
    __tablename__ = "films"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    genre = Column(String(50), nullable=False)
    year = Column(Integer(), nullable=False)
    director = Column(String(50), nullable=False)


Base.metadata.create_all(engine)
