from datos.conexion import Session
from objetos import Vuelos
from sqlalchemy import func

sesion = Session()

def obtener_datos_vuelos():
    listado_vuelos = sesion.query(Vuelos).all()
    if listado_vuelos:
        for vuelos in listado_vuelos:
            print(f"Código Vuelo: {vuelos.id}, Origen: {vuelos.origen}, Destino: {vuelos.destino}, Fecha: {vuelos.fecha}, Hora: {vuelos.hora}, Avión: {vuelos.avion}, Asientos Disponibles: {vuelos.asientos_disponibles}")