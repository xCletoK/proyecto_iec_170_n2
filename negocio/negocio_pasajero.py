from prettytable import PrettyTable
from auxiliares.normalizar_cadena import normalizar_cadena
from datos.obtener_datos import obtener_datos_objetos
from modelos import Pasajero

def listado_pasajeros():
    tabla_pasajeros = PrettyTable()
    tabla_pasajeros.field_names = ["N°", "RUT", "Nombre", "Numero Pasaporte", "Nacionalidad"]
    listado_pasajeros = obtener_datos_objetos(Pasajero)
    if listado_pasajeros:
        for pasajero in listado_pasajeros:
            tabla_pasajeros.add_row(
                [pasajero.id_pasajero, pasajero.rut, pasajero.nombre, pasajero.numero_pasaporte, pasajero.nacionalidad])
        print(tabla_pasajeros)

def obtener_pasajero_nombre(nombre_pasajero):
    listado_pasajeros = obtener_datos_objetos(Pasajero)
    pasajero_encontrado = None
    if listado_pasajeros:
        for pasajero in listado_pasajeros:
            if normalizar_cadena(pasajero.nombre) == normalizar_cadena(nombre_pasajero):
                pasajero_encontrado = pasajero
                break
    return pasajero_encontrado