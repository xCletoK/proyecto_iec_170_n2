from datos.conexion import sesion
from modelos.boleto import Boleto
from auxiliares.normalizar_cadena import normalizar_cadena

def obtener_datos_objetos(objeto):
    listado_objetos = sesion.query(Boleto).all()
    if len(listado_objetos) > 0:
        return listado_objetos
    
def obtener_datos_boleto(datos_boleto):
    listado_boletos = obtener_datos_objetos(Boleto)
    boleto_encontrado = None
    if listado_boletos:
        for boleto in listado_boletos:
            if normalizar_cadena(boleto.datos_boleto) == normalizar_cadena(datos_boleto):
                boleto_encontrado = boleto
                break
    return boleto_encontrado