from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from app.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey ,TIMESTAMP , Float

class  Admin(Base):
    __tablename__ = 'admin'
    id = Column(Integer , primary_key=True , nullable=False)
    name = Column(String(50) , nullable=False)
    username = Column(String(50) , unique=True , nullable=False)
    password = Column(String(50) , nullable=False)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer , primary_key=True , nullable=False)
    name = Column(String(50) , nullable=False)
    username = Column(String(50) , unique=True , nullable=False)
    password = Column(String(50) , nullable=False)
    admin_id = Column(Integer , ForeignKey('admin.id') , nullable=False)
    balance_id = Column(Integer , ForeignKey('balance.id') , nullable=False)
class Guest(Base):
    __tablename__ = 'guest'
    id = Column(Integer , primary_key=True , nullable=False)
    name = Column(String(50) , nullable=False)
    username = Column(String(50) , unique=True , nullable=False)
    password = Column(String(50) , nullable=False)
    user_id = Column(Integer , ForeignKey('user.id') , nullable=False)
class Guest_list(Base):
    __tablename__ = 'guest_list'
    id = Column(Integer , primary_key=True , nullable=False)
    guest_id = Column(Integer , ForeignKey('guest.id') , nullable=False)
    station_list = Column(String(2000) , nullable=False)
class region(Base):
    __tablename__ = 'region'
    id = Column(Integer , primary_key=True , nullable=False)
    name = Column(String(100) , nullable=False)

class discret(Base):
    __tablename__ = 'discret'
    id = Column(Integer , primary_key=True , nullable=False)
    name = Column(String(100) , nullable=False)
    region_id = Column(Integer , ForeignKey('region.id'), nullable=False)
class balance(Base):
    __tablename__ = 'balance'
    id = Column(Integer , primary_key=True , nullable=False)
    name = Column(String(100) , nullable=False)
    region_id = Column(Integer , ForeignKey('region.id'), nullable=False)

class Station(Base):
    __tablename__ = 'station'
    id = Column(Integer , primary_key=True , nullable=False)
    admin_id = Column(Integer , ForeignKey('admin.id') , nullable=False)
    name = Column(String(100) , nullable=False)
    region_id = Column(Integer , ForeignKey('region.id'), nullable=False)
    discret_id = Column(Integer , ForeignKey('discret.id'), nullable=False)
    balance_id = Column(Integer , ForeignKey('balance.id'), nullable=False)
    lan = Column(Float , nullable=False)
    lon = Column(Float , nullable=False)
    imei = Column(String(20) , nullable=False)
    proshivka = Column(String(20) , nullable=False)
    update = Column(TIMESTAMP , nullable=False)
    create = Column(TIMESTAMP , nullable=False)
class DataWater(Base):
    __tablename__ = 'data_water'
    id = Column(Integer , primary_key=True , nullable=False)
    station_id = Column(Integer , ForeignKey('station.id'), nullable=False)
    level = Column(Float , nullable=False)
    flow = Column(Float , nullable=False)
    corec = Column(Integer , nullable=False)
    time = Column(String , nullable=False)
class DataWaterHour(Base):
    __tablename__ = 'data_water_hour'
    id = Column(Integer , primary_key=True , nullable=False)
    station_id = Column(Integer , ForeignKey('station.id'), nullable=False)
    level = Column(Float , nullable=False)
    flow = Column(Float , nullable=False)
    time = Column(String , nullable=False)

class DataWell(Base):
    __tablename__ = 'data_well'
    id = Column(Integer , primary_key=True , nullable=False)
    station_id = Column(Integer , ForeignKey('station.id'), nullable=False)
    level = Column(Float , nullable=False)
    meloration = Column(Float , nullable=False)
    temp = Column(Float , nullable=False)
    time = Column(String , nullable=False)

class DataWellHour(Base):
    __tablename__ = 'data_well_hour'
    id = Column(Integer , primary_key=True , nullable=False)
    station_id = Column(Integer , ForeignKey('station.id'), nullable=False)
    level = Column(Float , nullable=False)
    meloration = Column(Float , nullable=False)
    time = Column(String , nullable=False)


class InfoWater(Base):
    __tablename__ = 'info_water'
    id = Column(Integer , primary_key=True , nullable=False)
    station_id = Column(Integer , ForeignKey('station.id'), nullable=False)
    battery = Column(Integer , nullable=False)
    signal = Column(Integer , nullable=False)
    solar = Column(Integer , nullable=False)
    time = Column(String , nullable=False)

class InfoWell(Base):
    __tablename__ = 'info_well'
    id = Column(Integer , primary_key=True , nullable=False)
    station_id = Column(Integer , ForeignKey('station.id'), nullable=False)
    battery = Column(Integer , nullable=False)
    signal = Column(Integer , nullable=False)
    solar = Column(Integer , nullable=False)
    time = Column(String , nullable=False)














"""
class Data(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True, nullable=False)
    data = Column(Integer, nullable=False)
    time = Column(String, nullable=False)


class Orta(Base):
    __tablename__ = 'orta'
    id = Column(Integer, primary_key=True, nullable=False)
    data = Column(Integer, nullable=False)
    time = Column(String, nullable=False)

class FlowOnline(Base):
    __tablename__ = 'flowonline'
    id = Column(Integer, primary_key=True, nullable=False)
    sped = Column(Float,nullable = False)
    flowsped = Column(Float,nullable = False)
    time = Column(String, nullable=False)
class FlowHour(Base):
    __tablename__ = 'flowhour'
    id = Column(Integer, primary_key=True, nullable=False)
    sped = Column(Float,nullable=False)
    flowsped = Column(Float,nullable=False)
    time = Column(String, nullable=False)

class DataNasos(Base):
    __tablename__ = 'datanasos'
    id = Column(Integer, primary_key=True, nullable=False)
    sped = Column(Float,nullable=False)
    flowsped = Column(Float,nullable=False)
    time = Column(String, nullable=False)
"""