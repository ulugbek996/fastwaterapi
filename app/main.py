from typing import Optional , List
from fastapi import FastAPI , Depends
from app import models ,schemas
from app.database import  engine, get_db
from sqlalchemy.orm import  Session
from fastapi.middleware.cors import CORSMiddleware
from app.routers import data , sped
models.Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(data.router)
app.include_router(sped.router)



@app.get("/")
def root():
    return {"message": "Smart Water Api"}