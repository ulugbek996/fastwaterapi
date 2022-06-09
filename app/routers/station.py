from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from app import  models, schemas
from app.database import get_db
from sqlalchemy import func
# from sqlalchemy.sql.functions import func

router = APIRouter(
    prefix="/station",
    tags=['Station']
)
@router.get("/regions" , response_model=List[schemas.Regions])
def get_regions(db: Session = Depends(get_db)):
    regions = db.query(models.region).all()
    return regions
@router.get("/discret/{region_id}" , response_model=List[schemas.Discret])
def get_discret(region_id: int, db: Session = Depends(get_db)):
    discret = db.query(models.discret).filter(models.discret.region_id == region_id).all()
    return discret
@router.get("/balance/{region_id}" , response_model=List[schemas.Balance])
def get_balance(region_id: int, db: Session = Depends(get_db)):
    balance = db.query(models.balance).filter(models.balance.region_id == region_id).all()
    return balance


@router.get("/")
def root():
    return {"message": "station"}

@router.get("/last" , response_model=schemas.Station) #, response_model=schemas.DataWater
def test_post(db: Session = Depends(get_db)):
    post = db.query(models.Station).order_by(models.Station.id.desc()).first()
    #post = db.query(models.Data).first()
    return post

@router.post("/" , status_code=status.HTTP_201_CREATED)
def station_post( post: schemas.StationCreate, db: Session = Depends(get_db)):
    new_post = models.Station(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post