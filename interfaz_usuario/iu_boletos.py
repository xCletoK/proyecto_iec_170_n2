def ingresar_datos_boleto():
    numero_asiento = input("Ingrese el número de asiento: ")
    fecha_compra = input("Ingrese la fecha de compra (YYYY-MM-DD): ")
    tarifa = float(input("Ingrese la tarifa del boleto: "))
    cod_vuelo = input("Ingrese el código del vuelo: ")
    rut_pasajero = input("Ingrese el RUT del pasajero: ")
    return (numero_asiento, fecha_compra, tarifa, cod_vuelo, rut_pasajero)