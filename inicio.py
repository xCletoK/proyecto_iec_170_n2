from datos.conexion import Session
from datos.obtener_datos import obtener_datos_objetos, obtener_datos_boleto
from interfaz_usuario.iu_boletos import ingresar_datos_boleto
from prettytable import PrettyTable
from modelos.boleto import Boleto

def listado_boletos():
    tabla_boletos = PrettyTable()
    tabla_boletos.field_names = ["ID Boleto", "Numero Asiento", "Fecha Compra", "Tarifa", "Cod Vuelo", "RUT Pasajero"]
    listado_boletos = obtener_datos_objetos(Boleto)
    if listado_boletos:
        for boleto in listado_boletos:
            tabla_boletos.add_row(
                [boleto.ID, boleto.numero_asiento, boleto.fecha_compra, boleto.tarifa, boleto.cod_vuelo, boleto.rut_pasajero])
            print(tabla_boletos)

sesion = Session()

def insertar_boleto():
    numero_asiento = input("Ingrese el número de asiento: ")
    fecha_compra = input("Ingrese la fecha de compra (YYYY-MM-DD): ")
    tarifa = float(input("Ingrese la tarifa del boleto: "))
    cod_vuelo = input("Ingrese el código del vuelo: ")
    rut_pasajero = input("Ingrese el RUT del pasajero: ")

    respuesta = obtener_datos_boleto(boleto)
    if respuesta == None:
        nuevo_boleto = Boleto(numero_asiento=numero_asiento.title(),
                              fecha_compra=fecha_compra.title(),
                              tarifa=tarifa.title(),
                              cod_vuelo=cod_vuelo.title(),
                              rut_pasajero=rut_pasajero.title())
        insertar_boleto(nuevo_boleto)
    else:
        print("El boleto ya existe en la base de datos.")

def modificar_boleto():
    boleto = input("Ingrese el ID del boleto a modificar: ")

    boleto_encontrado = obtener_datos_boleto(boleto)
    if boleto_encontrado:
        nuevo_numero_asiento = input("Ingrese el nuevo número de asiento: ")
        if nuevo_numero_asiento != '':
            nuevo_cod_vuelo = input("Ingrese el nuevo código de vuelo: ")
        if nuevo_cod_vuelo != '':
            nuevo_rut_pasajero = input("Ingrese el nuevo RUT del pasajero: ")
        if nuevo_rut_pasajero != '':
        modificar_objeto()

modificar_boleto()