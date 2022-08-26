from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import Optional,List
from database import Session
from get import specific_result,all_results
import models


app = FastAPI()

class Position(BaseModel):
    id: int
    lat: float
    longi:float


db = Session()

@app.get("/", status_code=200)
def init():
    return "/docs na url para ser direcionado para a área de testes do fastapi"

@app.get("/get", response_model=List[Position], 
        status_code=200)
def get_all_positions():
    return all_results()

@app.get("/get/{id}")
def get_specific_positions(id: int):
    return specific_result(id)

@app.post('/insere', response_model=Position, 
            status_code=status.HTTP_201_CREATED)
def insere_position(position: Position):
    new_device = models.Devices(
        id=position.id
    )
    new_location = models.Locations(
        lat=position.lat,
        longi=position.longi
    )
    db.add(new_device)
    db.commit()
    db.add(new_location)
    db.commit()
    return position

