from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class Pasajero(base):
    __tablename__ = 'pasajero'

    rut = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    num_pasajero = Column(Integer, nullable=True)
    nacionalidad = Column(String(50), nullable=True)

class Pasajero():
    def __init__(self, rut, nombre, num_pasajero, nacionalidad):
        self.rut = rut
        self.nombre = nombre
        self.num_pasajero = num_pasajero
        self.nacionalidad = nacionalidad