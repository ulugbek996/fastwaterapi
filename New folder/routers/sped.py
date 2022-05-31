from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional

from sqlalchemy import func
# from sqlalchemy.sql.functions import func
from .. import models, schemas
from ..database import get_db
router = APIRouter(
    prefix="/sped",
    tags=['Sped']
)


@router.get("/", response_model=List[schemas.Online] )
def test_post(db: Session = Depends(get_db)):
    #post = db.query(models.Data).all()
    post = db.query(models.FlowOnline).order_by(models.FlowOnline.id.desc()).limit(48).all()
    return post
@router.get("/last" , response_model=schemas.Hour )
def test_post(db: Session = Depends(get_db)):
    post = db.query(models.FlowHour).order_by(models.FlowHour.id.desc()).first()
    #post = db.query(models.Data).first()
    return post