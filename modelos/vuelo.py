from sqlalchemy import Column, Integer, String, Date, Time
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()




class Vuelo(base):
    __tablename__ = 'vuelo'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    origen = Column(String(10), nullable=False)
    destino = Column(String(10), nullable=False)
    fecha_salida = Column(Date, nullable=False)
    hora_salida = Column(Time, nullable=False)
    fecha_llegada = Column(Date, nullable=False)
    hora_llegada = Column(Time, nullable=False)
    cantidad_asientos = Column(Integer, nullable=False)

class Vuelo():
    def __init__(self, origen, destino, fecha_salida, hora_salida, fecha_llegada, hora_llegada, cantidad_asientos):
        self.origen = origen
        self.destino = destino
        self.fecha_salida = fecha_salida
        self.hora_salida = hora_salida
        self.fecha_llegada = fecha_llegada
        self.hora_llegada = hora_llegada
        self.cantidad_asientos = cantidad_asientos