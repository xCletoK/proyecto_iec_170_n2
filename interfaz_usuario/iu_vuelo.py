def ingresar_origen():
    return input("Ingrese origen (código 3 letras): ").strip().upper()

def ingresar_destino():
    return input("Ingrese destino (código 3 letras): ").strip().upper()

def ingresar_fecha_salida():
    return input("Ingrese fecha salida (YYYY-MM-DD): ").strip()

def ingresar_hora_salida():
    return input("Ingrese hora salida (HH:MM:SS): ").strip()

def ingresar_cantidad_asientos():
    return int(input("Ingrese cantidad de asientos: ").strip())