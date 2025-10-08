USE iec_170_n2;

CREATE TABLE vuelo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    origen VARCHAR(10) NOT NULL,
    destino VARCHAR(10) NOT NULL,
    fecha_salida DATE NOT NULL,
    hora_salida TIME NOT NULL,
    fecha_llegada DATE NOT NULL,
    hora_llegada TIME NOT NULL,
    cantidad_asientos INT NOT NULL
);

CREATE TABLE IF NOT EXISTS pasajero (
    rut VARCHAR(10) PRIMARY KEY NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    num_pasaporte VARCHAR(20),
    nacionalidad VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS boleto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero_asiento INT(2) NOT NULL,
    fecha_compra DATE NOT NULL,
    tarifa DECIMAL(10,2) NOT NULL,
    cod_vuelo INT NOT NULL,
    rut_pasajero VARCHAR(10) NOT NULL,
    FOREIGN KEY (cod_vuelo) REFERENCES vuelo(id) ON DELETE CASCADE,
    FOREIGN KEY (rut_pasajero) REFERENCES pasajero(rut) ON DELETE CASCADE