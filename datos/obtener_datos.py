from datos.conexion import Session
from objetos import Vuelo
from sqlalchemy import func

sesion = Session()

def obtener_datos_vuelo():
    listado_vuelos = sesion.query(Vuelo).all()
    if listado_vuelos:
        for vuelo in listado_vuelos:
            print(f"Código: {vuelo.id}, Origen: {vuelo.origen}, Destino: {vuelo.destino}, Fecha Salida: {vuelo.fecha_salida}, Hora Salida: {vuelo.hora_salida}, Fecha Llegada: {vuelo.fecha_llegada}, Hora Llegada: {vuelo.hora_llegada}, Cantidad Asientos {vuelo.cantidad_asientos}")
