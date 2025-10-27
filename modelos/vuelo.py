from sqlalchemy import Column, Integer, String, Date, Time
from modelos.base import Base

class Vuelo(Base):
    __tablename__ = 'vuelo'

    id = Column(Integer, primary_key=True, autoincrement=True)
    origen = Column(String(10), nullable=False)
    destino = Column(String(10), nullable=False)
    fecha_salida = Column(Date, nullable=False)
    hora_salida = Column(Time, nullable=False)
    fecha_llegada = Column(Date, nullable=False)
    hora_llegada = Column(Time, nullable=False)
    cantidad_asientos = Column(Integer, nullable=False)
