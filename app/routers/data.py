from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from app import  models, schemas
from app.database import get_db
from sqlalchemy import func
# from sqlalchemy.sql.functions import func

router = APIRouter(
    prefix="/data",
    tags=['Data']
)

@router.get("/")
def root():
    return {"message": "Data"}

@router.get("/last" , response_model=List[schemas.DataWater]) #, response_model=schemas.DataWater
def las_data(db: Session = Depends(get_db)):
    userstation = db.query(models.Userstation).filter(models.Userstation.user_id == 2).first()
    station = (userstation.stations)
    #print(type(station))
    #station = db.query(models.Station).filter(models.Station.balance_id == 700).all()
    #stations = []
    #for i in station:
        #stations.append(i.id)
    stations = station.split(',')
    #post = db.query(models.DataWater).order_by(models.DataWater.id.desc()).first()
    post = db.query(models.DataWater).filter(models.DataWater.station_id.in_(stations)).all()
    #session.query(MyUserClass).filter(MyUserClass.id.in_((123,456))).all()
    #post = db.query(models.Data).first()
    return post
@router.get("/hour/{station_id}" , response_model=List[schemas.DataWaterHour]) #, response_model=schemas.DataWater
def las_data_hour(station_id: int, db: Session = Depends(get_db)):
    post = db.query(models.DataWaterHour).filter(models.DataWaterHour.station_id == station_id).all()
    return post


"""
@router.get("/", response_model=List[schemas.Orta] )
def test_post(db: Session = Depends(get_db)):
    #post = db.query(models.Data).all()
    post = db.query(models.Data).order_by(models.Data.id.desc()).limit(48).all()
    return post
@router.get("/1", response_model=List[schemas.Orta] )
def test_post(db: Session = Depends(get_db)):
    #post = db.query(models.Data).all()
    post = db.query(models.Orta).order_by(models.Orta.id.desc()).limit(48).all()
    return post
@router.get("/last" , response_model=schemas.Data )
def test_post(db: Session = Depends(get_db)):
    post = db.query(models.Data).order_by(models.Data.id.desc()).first()
    #post = db.query(models.Data).first()
    return post

"""