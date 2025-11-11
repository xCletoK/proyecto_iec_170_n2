from datos import obtener_datos_objetos
from auxiliares import normalizar_cadena
from modelos.vuelo import Vuelo
from modelos.boleto import Boleto

def obtener_vuelo_por_id(id_vuelo):
    return obtener_datos_objetos(Vuelo).filter(Vuelo.id == id_vuelo).first()

def verificar_capacidad_vuelo(id_vuelo):
    vuelo = obtener_vuelo_por_id(id_vuelo)
    if not vuelo:
        return False
    

    boletos_vendidos = obtener_datos_objetos(Boleto).filter(
        Boleto.cod_vuelo == id_vuelo
    ).count()
    
    return boletos_vendidos < vuelo.cantidad_asientos

def verificar_asiento_disponible(id_vuelo, numero_asiento):
    boleto_existente = obtener_datos_objetos(Boleto).filter(
        Boleto.cod_vuelo == id_vuelo,
        Boleto.numero_asiento == numero_asiento
    ).first()
    
    return boleto_existente is None