from datos.conexion import sesion

def insertar_objeto(objeto):
    sesion.add(objeto)
    sesion.commit()