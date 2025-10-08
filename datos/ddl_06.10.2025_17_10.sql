use  iec_170_n2;

CREATE TABLE viajes(
    id INTEGER auto_increment PRIMARY KEY,
    origen char(10) not null,
    destino char(10) not null,
    fecha_salida date(5),

    constraint pk_viajes primary key (id)

);

create table boleto if not exist(
    id integer auto_increment primary key,
    numero_asiento integer(2) not null,
    fecha_compra date,
    tarifa integer,
    rut_pasajero varchar(10),

    constraint pk_boleto primary key (id),
    constraint fk_boleto_viajes foreign key (id_viaje) references viajes(id)

);

create table pasajero if not exist(
    rut varchar(10) primary key not null,
    nombres varchar(20) not null,
    fecha_nacimiento date,
    direccion varchar not null,

    constraint pk_pasajero primary key (rut)
    constraint fk_pasajero_boleto foreing key id_boleto references boleto(id)
);
