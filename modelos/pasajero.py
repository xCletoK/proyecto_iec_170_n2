from sqlalchemy import Column, String, Boolean
from modelos.base import Base

class Pasajero(Base):
    __tablename__ = 'pasajero'
    rut = Column(String(10), primary_key=True)
    nombre = Column(String(50), nullable=False)
    num_pasaporte = Column(String(20))
    nacionalidad = Column(String(30))
    habilitado = Column(Boolean, default=True, nullable=False)