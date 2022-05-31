from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from app.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey ,TIMESTAMP , Float














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