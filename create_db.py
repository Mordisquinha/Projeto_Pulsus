from database import Base, engine
from models import Devices, Locations

print("criando database")
Base.metadata.create_all(engine)