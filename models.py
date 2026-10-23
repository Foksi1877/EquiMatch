from sqlalchemy import Column, Integer, String, Float, Text, Boolean
from database import Base


class Stable(Base):
    __tablename__ = "stables"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    address = Column(String)
    lat = Column(Float)
    lon = Column(Float)

    # Цены
    price_board = Column(Integer, default=0)
    price_training = Column(Integer, default=0)

    # Текстовые данные
    discipline = Column(String)
    description = Column(Text)
    contact = Column(String)

    # Инфраструктура (True/False)
    has_warm_wash = Column(Boolean, default=False)  # Теплая мойка
    has_summer_wash = Column(Boolean, default=False)  # Летняя уличная мойка
    has_summer_stables = Column(Boolean, default=False)
    has_solarium = Column(Boolean, default=False)
    has_indoor_arena = Column(Boolean, default=False)
    has_levalds = Column(Boolean, default=False)
    has_vet = Column(Boolean, default=False)