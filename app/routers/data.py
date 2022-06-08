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

@router.get("/last" , response_model=schemas.DataWater) #, response_model=schemas.DataWater
def test_post(db: Session = Depends(get_db)):
    post = db.query(models.DataWater).order_by(models.DataWater.id.desc()).first()
    #post = db.query(models.Data).first()
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