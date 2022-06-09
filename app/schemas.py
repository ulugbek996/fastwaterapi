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

class Station(BaseModel):
    id: int
    name: str
    admin_id: int
    region_id: int
    discret_id: int
    balance_id: int
    lan: float
    lon: float
    imei: str
    proshivka: str
    update: datetime
    create: datetime
    class Config:
        orm_mode = True

class StationCreate(BaseModel):
    name: str
    admin_id: int
    region_id: int
    discret_id: int
    balance_id: int
    lan: float
    lon: float
    imei: str
    proshivka: str
    update: datetime
    create: datetime
    class Config:
        orm_mode = True
class Regions(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True
class Discret(BaseModel):
    id: int
    name: str
    region_id: int
    class Config:
        orm_mode = True
class Balance(BaseModel):
    id: int
    name: str
    region_id: int
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