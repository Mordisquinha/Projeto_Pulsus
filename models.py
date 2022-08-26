from database import Base
from sqlalchemy import Integer, Float, Column

class Devices(Base):
    __tablename__ = 'devices'
    chave = Column(Integer, primary_key=True)
    id = Column(Integer,nullable=False)

class Locations(Base):
    __tablename__ = 'locations'
    chave = Column(Integer, primary_key=True)
    lat = Column(Float,nullable=False)
    longi = Column(Float,nullable=False)