from typing import Optional

from pydantic import BaseModel ,EmailStr
from datetime import datetime


class DataWater(BaseModel):
    station_id: int
    level: float
    flow: float
    corec: int
    time: str
    class Config:
        orm_mode = True

class DataWaterHour(BaseModel):
    station_id: int
    level: float
    flow: float
    time: str
    class Config:
        orm_mode = True
class DataWell(BaseModel):
    level: float
    meloration: float
    temp: float
    time: str
    class Config:
        orm_mode = True
class DataWellHour(BaseModel):
    level: float
    meloration: float
    time: str
    class Config:
        orm_mode = True





"""
class Data(BaseModel):
    id: int
    data: int
    time: str
    class Config:
        orm_mode = True

class Orta(BaseModel):
    id: int
    data: int
    time: str
    class Config:
        orm_mode = True

class Online(BaseModel):
    id: int
    sped: float
    flowsped: float
    time: str
    class Config:
        orm_mode = True

class Hour(BaseModel):
    id: int
    sped: float
    flowsped: float
    time: str
    class Config:
        orm_mode = True
"""