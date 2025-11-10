from prettytable import PrettyTable
from modelos.boleto import Boleto
from datos import modificar_objeto, obtener_datos_objetos, insertar_objeto, eliminar_objeto
from auxiliares import normalizar_cadena
from negocio.negocio_vuelo import obtener_vuelo_codigo
from negocio.negocio_pasajero import obtener_pasajero_rut
from interfaz_usuario import 


def listado_boletos():
    tabla_boletos = PrettyTable()
    tabla_boletos.field_names = ["ID Boleto", "Numero Asiento", "Fecha Compra", "Tarifa", "Cod Vuelo", "RUT Pasajero"]
    listado_boletos = obtener_datos_objetos(Boleto)
    if listado_boletos:
        for boleto in listado_boletos:
            tabla_boletos.add_row(
                [boleto.ID, boleto.numero_asiento, boleto.fecha_compra, boleto.tarifa, boleto.cod_vuelo, boleto.rut_pasajero])
        print(tabla_boletos)


def obtener_boleto_id(id_boleto):
    listado_boletos = obtener_datos_objetos(Boleto)
    boleto_encontrado = None
    if listado_boletos:
        for boleto in listado_boletos:
            if boleto.ID == id_boleto:
                boleto_encontrado = boleto
                break
    return boleto_encontrado


def insertar_boleto():
    numero_asiento = input("Ingrese el número de asiento: ")
    fecha_compra = input("Ingrese la fecha de compra (YYYY-MM-DD): ")
    tarifa = float(input("Ingrese la tarifa del boleto: "))
    cod_vuelo = input("Ingrese el código del vuelo: ")
    rut_pasajero = input("Ingrese el RUT del pasajero: ")

    boleto_encontrado = obtener_boleto_id(numero_asiento)
    if boleto_encontrado == None:
        nuevo_boleto = Boleto(numero_asiento=numero_asiento,
                              fecha_compra=fecha_compra,
                              tarifa=tarifa,
                              cod_vuelo=cod_vuelo,
                              rut_pasajero=rut_pasajero)
        insertar_objeto(nuevo_boleto)
    else:
        print("El boleto ya existe en la base de datos.")


def modificar_boleto():
    id_boleto = input("Ingrese el ID del boleto a modificar: ")

    boleto_encontrado = obtener_boleto_id(id_boleto)
    if boleto_encontrado:
        nuevo_numero_asiento = input("Ingrese el nuevo número de asiento: ")
        nuevo_cod_vuelo = input("Ingrese el nuevo código de vuelo: ")
        nuevo_rut_pasajero = input("Ingrese el nuevo RUT del pasajero: ")
        
        if nuevo_numero_asiento != '':
            boleto_encontrado.numero_asiento = nuevo_numero_asiento
        if nuevo_cod_vuelo != '':
            boleto_encontrado.cod_vuelo = nuevo_cod_vuelo
        if nuevo_rut_pasajero != '':
            boleto_encontrado.rut_pasajero = nuevo_rut_pasajero
            
        modificar_objeto()


def eliminado_logico_boleto():
    id_boleto = input("Ingrese el ID del boleto: ")

    boleto_encontrado = obtener_boleto_id(id_boleto)
    if boleto_encontrado:
        boleto_encontrado.habilitado = False
        modificar_objeto()


def eliminado_fisico_boleto():
    while True:
        id_boleto = input("Ingrese el ID del boleto: ")

        boleto_encontrado = obtener_boleto_id(id_boleto)
        if boleto_encontrado:
            eliminar_objeto(boleto_encontrado)
            break
        else:
            print('Boleto NO existe, vuelva a intentarlo.')