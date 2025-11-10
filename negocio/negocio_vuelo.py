from datos import obtener_datos_objetos
from auxiliares import normalizar_cadena
from modelo.vuelo import Vuelo

def obtener_vuelo_codigo(buscar_vuelo):
    listado_vuelos = obtener_datos_objetos(Vuelo)
    vuelo_encontrado = None
    if listado_vuelos:
        for vuelo in listado_vuelos:
            if normalizar_cadena(vuelo.codigo) == normalizar_cadena(buscar_vuelo):
                vuelo_encontrado = vuelo
                break
        return vuelo_encontrado