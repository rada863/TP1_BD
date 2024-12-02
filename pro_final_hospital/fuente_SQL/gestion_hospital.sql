
-- Tabla Paciente
CREATE TABLE Paciente (
    id_paciente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    edad INT,
    direccion VARCHAR(100),
    telefono VARCHAR(20),
    email VARCHAR(100)
);

-- Tabla Medico
CREATE TABLE Medico (
    id_medico INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    especialidad VARCHAR(50),
    telefono VARCHAR(20),
    email VARCHAR(100)
);

-- Tabla Turno
CREATE TABLE Turno (
    id_turno INT AUTO_INCREMENT PRIMARY KEY,
    id_paciente INT,
    id_medico INT,
    fecha_hora DATETIME,
    estado VARCHAR(20),
    FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente),
    FOREIGN KEY (id_medico) REFERENCES Medico(id_medico)
);

-- Insertar datos iniciales en Paciente
INSERT INTO Paciente (nombre, apellido, edad, direccion, telefono, email) VALUES
('Juan', 'Pérez', 30, 'Calle Falsa 123', '+5491112345678', 'juan.perez@example.com'),
('María', 'González', 45, 'Av. Siempre Viva 456', '+5491198765432', 'maria.gonzalez@example.com'),
('Carlos', 'López', 28, 'Calle 7 Nro 89', '+5491145678901', 'carlos.lopez@example.com'),
('Ana', 'Martínez', 35, 'Pasaje Las Flores 12', '+5491123456789', 'ana.martinez@example.com'),
('Luis', 'García', 50, 'Boulevard Central 210', '+5491167890123', 'luis.garcia@example.com'),
('Sofía', 'Rodríguez', 22, 'Callejón del Sol 33', '+5491178901234', 'sofia.rodriguez@example.com'),
('Miguel', 'Fernández', 40, 'Plaza Mayor 78', '+5491189012345', 'miguel.fernandez@example.com'),
('Laura', 'Sánchez', 27, 'Avenida del Libertador 500', '+5491123450987', 'laura.sanchez@example.com'),
('Fernando', 'Ramírez', 33, 'Camino Real 250', '+5491132109876', 'fernando.ramirez@example.com'),
('Lucía', 'Torres', 38, 'Ruta Provincial Km 45', '+5491145674321', 'lucia.torres@example.com');

-- Insertar datos iniciales en Medico
INSERT INTO Medico (nombre, apellido, especialidad, telefono, email) VALUES
('Diego', 'Muñoz', 'Cardiología', '+5491198765432', 'dr.diego.munoz@hospital.com'),
('Elena', 'Herrera', 'Neurología', '+5491112345678', 'dra.elena.herrera@hospital.com'),
('Ricardo', 'Suárez', 'Pediatría', '+5491123456789', 'dr.ricardo.suarez@hospital.com'),
('Patricia', 'Gutiérrez', 'Dermatología', '+5491134567890', 'dra.patricia.gutierrez@hospital.com'),
('Andrés', 'Rojas', 'Traumatología', '+5491145678901', 'dr.andres.rojas@hospital.com'),
('Gabriela', 'Molina', 'Ginecología', '+5491156789012', 'dra.gabriela.molina@hospital.com'),
('Javier', 'Jiménez', 'Oftalmología', '+5491167890123', 'dr.javier.jimenez@hospital.com'),
('Laura', 'Morales', 'Otorrinolaringología', '+5491178901234', 'dra.laura.morales@hospital.com'),
('Fernando', 'Cruz', 'Oncología', '+5491189012345', 'dr.fernando.cruz@hospital.com'),
('Silvia', 'Ortiz', 'Endocrinología', '+5491190123456', 'dra.silvia.ortiz@hospital.com');

-- Insertar datos iniciales en Turno
-- Generar 10 turnos por cada paciente (total 100 turnos)
INSERT INTO Turno (id_paciente, id_medico, fecha_hora, estado) VALUES
-- Turnos del Paciente 1
(1, 1, '2023-12-01 09:00:00', 'Programado'),
(1, 2, '2023-12-03 10:00:00', 'Programado'),
(1, 3, '2023-12-05 11:00:00', 'Programado'),
(1, 4, '2023-12-07 12:00:00', 'Programado'),
(1, 5, '2023-12-09 13:00:00', 'Programado'),
(1, 6, '2023-12-11 14:00:00', 'Programado'),
(1, 7, '2023-12-13 15:00:00', 'Programado'),
(1, 8, '2023-12-15 16:00:00', 'Programado'),
(1, 9, '2023-12-17 17:00:00', 'Programado'),
(1, 10, '2023-12-19 18:00:00', 'Programado'),
-- Turnos del Paciente 2
(2, 1, '2023-12-02 09:00:00', 'Programado'),
(2, 2, '2023-12-04 10:00:00', 'Programado'),
(2, 3, '2023-12-06 11:00:00', 'Programado'),
(2, 4, '2023-12-08 12:00:00', 'Programado'),
(2, 5, '2023-12-10 13:00:00', 'Programado'),
(2, 6, '2023-12-12 14:00:00', 'Programado'),
(2, 7, '2023-12-14 15:00:00', 'Programado'),
(2, 8, '2023-12-16 16:00:00', 'Programado'),
(2, 9, '2023-12-18 17:00:00', 'Programado'),
(2, 10, '2023-12-20 18:00:00', 'Programado'),
-- Turnos del Paciente 3
(3, 1, '2023-12-01 09:00:00', 'Programado'),
(3, 2, '2023-12-03 10:00:00', 'Programado'),
(3, 3, '2023-12-05 11:00:00', 'Programado'),
(3, 4, '2023-12-07 12:00:00', 'Programado'),
(3, 5, '2023-12-09 13:00:00', 'Programado'),
(3, 6, '2023-12-11 14:00:00', 'Programado'),
(3, 7, '2023-12-13 15:00:00', 'Programado'),
(3, 8, '2023-12-15 16:00:00', 'Programado'),
(3, 9, '2023-12-17 17:00:00', 'Programado'),
(4, 10,'2023-12-19 18:00:00', 'Programado'),
--realmente no creo que sea necesario completar los 10 pacientes o si?