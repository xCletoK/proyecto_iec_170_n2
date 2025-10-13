INSERT INTO pasajero (rut, nombre, num_pasaporte, nacionalidad)VALUES 
('12345678-9', 'Juan Pérez López', 'AB1234567', 'Española'),
('87654321-0', 'María García Ruiz', 'CD7654321', 'Mexicana'),
('11223344-5', 'Carlos López Mendoza', 'EF1122334', 'Argentina'),
('55667788-0', 'Ana Torres Silva', 'GH5566778', 'Española'),
('99887766-1', 'Pedro Ramírez Soto', 'IJ9988776', 'Chilena');

INSERT INTO vuelo (origen, destino, fecha_salida, hora_salida, fecha_llegada, hora_llegada, cantidad_asientos) VALUES 
('MAD', 'BCN', '2025-10-09', '08:00:00', '2025-10-09', '09:30:00', 150),
('MAD', 'BCN', '2025-10-10', '07:45:00', '2025-10-10', '09:15:00', 180),
('BCN', 'SVQ', '2025-10-11', '14:20:00', '2025-10-11', '16:50:00', 120),
('MAD', 'PAR', '2025-10-12', '09:30:00', '2025-10-12', '11:45:00', 200),
('SVQ', 'AGP', '2025-10-13', '11:00:00', '2025-10-13', '11:45:00', 90),
('BCN', 'ROM', '2025-10-14', '16:15:00', '2025-10-14', '18:30:00', 160);

INSERT INTO boleto (numero_asiento, fecha_compra, tarifa, cod_vuelo, rut_pasajero) VALUES 
(1, '2025-10-07', 89.50, 1, '12345678-9'),
(2, '2025-10-07', 89.50, 1, '87654321-0'),
(15, '2025-10-08', 125.00, 2, '11223344-5'),
(3, '2025-10-08', 95.75, 3, '55667788-0'),
(4, '2025-10-06', 210.00, 4, '99887766-1'),
(20, '2025-10-07', 45.00, 5, '12345678-9'),
(5, '2025-10-08', 145.25, 6, '87654321-0');