from datos.conexion import Session
from datos.obtener_datos import obtener_datos_objetos
from prettytable import PrettyTable

from modelos.vuelo import Vuelo
from modelos.pasajero import Pasajero
from modelos.boleto import Boleto


def listado_vuelos():
    tabla = PrettyTable()
    tabla.field_names = [
        "ID",
        "Origen",
        "Destino",
        "Fecha Salida",
        "Hora Salida",
        "Fecha Llegada",
        "Hora Llegada",
        "Asientos"
    ]
    lista = obtener_datos_objetos(Vuelo)
    if lista:
        for v in lista:
            tabla.add_row([
                v.id,
                v.origen,
                v.destino,
                v.fecha_salida,
                v.hora_salida,
                v.fecha_llegada,
                v.hora_llegada,
                v.cantidad_asientos
            ])
        print(tabla)


def listado_pasajeros():
    tabla = PrettyTable()
    tabla.field_names = [
        "RUT",
        "Nombre",
        "Número Pasaporte",
        "Nacionalidad"
    ]
    lista = obtener_datos_objetos(Pasajero)
    if lista:
        for p in lista:
            tabla.add_row([
                p.rut,
                p.nombre,
                p.num_pasaporte,
                p.nacionalidad
            ])
        print(tabla)


def listado_boletos():
    tabla = PrettyTable()
    tabla.field_names = [
        "ID",
        "Asiento",
        "Fecha Compra",
        "Tarifa",
        "Cod Vuelo",
        "RUT Pasajero"
    ]
    lista = obtener_datos_objetos(Boleto)
    if lista:
        for b in lista:
            tabla.add_row([
                b.id,
                b.numero_asiento,
                b.fecha_compra,
                b.tarifa,
                b.cod_vuelo,
                b.rut_pasajero
            ])
        print(tabla)


sesion = Session()


def insertar_boleto():
    numero_asiento = input("Ingrese número de asiento: ")
    fecha_compra = input("Ingrese fecha de compra (YYYY-MM-DD): ")
    tarifa = input("Ingrese tarifa: ")
    cod_vuelo = input("Ingrese ID vuelo: ")
    rut = input("Ingrese RUT pasajero: ")

    nuevo_boleto = Boleto(
        numero_asiento=numero_asiento,
        fecha_compra=fecha_compra,
        tarifa=tarifa,
        cod_vuelo=cod_vuelo,
        rut_pasajero=rut
    )

    sesion.add(nuevo_boleto)

    try:
        sesion.commit()
        print("El boleto se ha insertado correctamente.")
    except Exception as e:
        sesion.rollback()
        print(f"Error al insertar el boleto: {e}")
    finally:
        sesion.close()


# --- PRUEBA ---
# listado_vuelos()
# listado_pasajeros()
# listado_boletos()
insertar_boleto()
