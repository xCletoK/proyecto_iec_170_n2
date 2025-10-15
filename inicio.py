from datos.obtener_datos import obtener_datos_objetos
from prettytable import PrettyTable

from modelos.pasajero import Pasajero
from modelos.vuelo import Vuelo

def listado_vuelo():
    tabla_vuelo = PrettyTable()
    tabla_vuelo.field_names = ["ID", "Origen", "Destino", "Fecha Salida", "Hora Salida", "Fecha Llegada", "Hora Llegada", "Cantidad Pasajeros"]
    listado_vuelo = obtener_datos_objetos(Vuelo)
    if listado_vuelo:
        for vuelo in listado_vuelo:
            tabla_vuelo.add_row(
                [vuelo.id, vuelo.origen, vuelo.destino, vuelo.fecha_salida, vuelo.hora_salida, vuelo.fecha_llegada, vuelo.hora_llegada, vuelo.cantidad_pasajeros])
        print(tabla_vuelo)

def listado_pasajero():
    tabla_pasajero = PrettyTable()
    tabla_pasajero.field_names = ["RUT", "Nombre", "Número Pasaporte", "Nacionalidad"]
    listado_pasajero = obtener_datos_objetos(Pasajero)
    if listado_pasajero:
        for pasajero in listado_pasajero:
            tabla_pasajero.add_row(
                [pasajero.rut, pasajero.nombre, pasajero.num_pasaporte, pasajero.nacionalidad])
        print(tabla_pasajero)



#from interfaz_usuario import menu_principal
#menu_principal()from interfaz_usuario.menu_principal import menu_principal
#menu_principal()