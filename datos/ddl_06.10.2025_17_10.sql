USE iec_170_n2;

CREATE TABLE viajes if not exists(
    id INTEGER AUTO_INCREMENT,
    origen CHAR(50) NOT NULL,
    destino CHAR(50) NOT NULL,
    fecha_salida DATE(5),

    CONSTRAINT pk_viajes PRIMARY KEY (id)

)

CREATE TABLE direcciones IF NOT EXISTS(
    
)