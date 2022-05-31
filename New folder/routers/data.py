from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional

from sqlalchemy import func
# from sqlalchemy.sql.functions import func
from .. import models, schemas
from ..database import get_db
router = APIRouter(
    prefix="/data",
    tags=['Data']
)


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

