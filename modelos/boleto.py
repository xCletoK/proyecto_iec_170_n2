from sqlalchemy import Column, Integer, String, Date, DECIMAL, ForeignKey
from datos.conexion import Base

class Boleto(Base):
    __tablename__ = 'boleto'
    id = Column(Integer, primary_key=True, autoincrement=True)
    numero_asiento = Column(Integer, nullable=False)
    fecha_compra = Column(Date, nullable=False)
    tarifa = Column(DECIMAL(10, 2), nullable=False)

    cod_vuelo = Column(Integer, ForeignKey('vuelo.id'), nullable=False)
    rut_pasajero = Column(String(10), ForeignKey('pasajero.rut'), nullable=False)