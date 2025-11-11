from sqlalchemy import Column, Integer, String, Date, DECIMAL, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from modelos.base import Base

class Boleto(Base):
    __tablename__ = 'boleto'
    id = Column(Integer, primary_key=True, autoincrement=True)
    numero_asiento = Column(Integer, nullable=False)
    fecha_compra = Column(Date, nullable=False)
    tarifa = Column(DECIMAL(10, 2), nullable=False)
    cod_vuelo = Column(Integer, ForeignKey("vuelo.id"), nullable=False, index=True)
    rut_pasajero = Column(String(10), ForeignKey("pasajero.rut"), nullable=False, index=True)
    habilitado = Column(Boolean, default=True, nullable=False)