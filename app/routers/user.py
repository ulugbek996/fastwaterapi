from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional

from sqlalchemy import func
# from sqlalchemy.sql.functions import func


router = APIRouter(
    prefix="/user",
    tags=['User']
)
@router.get("/")
def root():
    return {"message": "User"}