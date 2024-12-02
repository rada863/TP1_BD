import sys
from app import create_app
from modelo.repositorio.paciente_repositorio import PacienteRepository
from modelo.repositorio.medico_repositorio import MedicoRepository
from modelo.repositorio.turno_repositorio import TurnoRepository

app = create_app()

def mostrar_menu():
    print("\n--- Sistema de Gestión de Hospital ---")
    print("1. Gestión de Pacientes")
    print("2. Gestión de Doctores")
    print("3. Manejo de Turnos")
    print("4. Búsquedas Avanzadas")
    print("5. Reporte de Turnos")
    print("6. Cancelación de Turnos")
    print("7. Salir")

def gestion_pacientes():
    print("\n--- Gestión de Pacientes ---")
    print("1. Registrar Paciente")
    print("2. Actualizar Paciente")
    print("3. Ver Paciente")
    print("4. Eliminar Paciente")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        edad = input("Edad: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        PacienteRepository.agregar_paciente(nombre, apellido, edad, direccion, telefono, email)
        print("Paciente registrado con éxito.")
    elif opcion == '2':
        id = input("ID del Paciente a actualizar: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        edad = input("Edad: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        PacienteRepository.modificar_paciente(id, nombre, apellido, edad, direccion, telefono, email)
        print("Paciente actualizado con éxito.")
    elif opcion == '3':
        id = input("ID del Paciente: ")
        paciente = PacienteRepository.mostrar_paciente(id)
        if paciente:
            print(paciente.to_dict())
        else:
            print("Paciente no encontrado.")
    elif opcion == '4':
        id = input("ID del Paciente a eliminar: ")
        if PacienteRepository.eliminar_paciente(id):
            print("Paciente eliminado con éxito.")
        else:
            print("Paciente no encontrado.")

def gestion_doctores():
    print("\n--- Gestión de Doctores ---")
    print("1. Agregar Doctor")
    print("2. Actualizar Doctor")
    print("3. Ver Doctor")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        especialidad = input("Especialidad: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        MedicoRepository.agregar_medico(nombre, apellido, especialidad, telefono, email)
        print("Doctor agregado con éxito.")
    elif opcion == '2':
        id = input("ID del Doctor a actualizar: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        especialidad = input("Especialidad: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        MedicoRepository.modificar_medico(id, nombre, apellido, especialidad, telefono, email)
        print("Doctor actualizado con éxito.")
    elif opcion == '3':
        id = input("ID del Doctor: ")
        doctor = MedicoRepository.mostrar_medico(id)
        if doctor:
            print(doctor.to_dict())
        else:
            print("Doctor no encontrado.")

def manejo_turnos():
    print("\n--- Manejo de Turnos ---")
    print("1. Programar Turno")
    print("2. Actualizar Turno")
    print("3. Cancelar Turno")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        id_paciente = input("ID del Paciente: ")
        id_medico = input("ID del Médico: ")
        fecha_hora = input("Fecha y Hora (AAAA-MM-DD HH:MM:SS): ")
        estado = input("Estado: ")
        TurnoRepository.programar_turno(id_paciente, id_medico, fecha_hora, estado)
        print("Turno programado con exito")


def manejo_turnos():
    print("\n--- Manejo de Turnos ---")
    print("1. Programar Turno")
    print("2. Actualizar Turno")
    print("3. Cancelar Turno")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        id_paciente = input("ID del Paciente: ")
        id_medico = input("ID del Médico: ")
        fecha_hora = input("Fecha y Hora (AAAA-MM-DD HH:MM:SS): ")
        estado = input("Estado: ")
        TurnoRepository.programar_turno(id_paciente, id_medico, fecha_hora, estado)
        print("Turno programado con éxito.")
    elif opcion == '2':
        id = input("ID del Turno a actualizar: ")
        id_paciente = input("ID del Paciente: ")
        id_medico = input("ID del Médico: ")
        fecha_hora = input("Fecha y Hora (AAAA-MM-DD HH:MM:SS): ")
        estado = input("Estado: ")
        TurnoRepository.actualizar_turno(id, id_paciente, id_medico, fecha_hora, estado)
        print("Turno actualizado con éxito.")
    elif opcion == '3':
        id = input("ID del Turno a cancelar: ")
        if TurnoRepository.cancelar_turno(id):
            print("Turno cancelado con éxito.")
        else:
            print("Turno no encontrado.")

def busquedas_avanzadas():
    print("\n--- Búsquedas Avanzadas ---")
    print("1. Buscar Paciente por Nombre")
    print("2. Buscar Médico por Especialidad")
    print("3. Buscar Paciente por ID")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        nombre = input("Nombre del Paciente: ")
        pacientes = PacienteRepository.buscar_pacientes_por_nombre(nombre)
        for paciente in pacientes:
            print(paciente.to_dict())
    elif opcion == '2':
        especialidad = input("Especialidad del Médico: ")
        medicos = MedicoRepository.buscar_medicos_por_especialidad(especialidad)
        for medico in medicos:
            print(medico.to_dict())
    elif opcion == '3':
        id = input("ID del Paciente: ")
        paciente = PacienteRepository.mostrar_paciente(id)
        if paciente:
            print(paciente.to_dict())
        else:
            print("Paciente no encontrado.")

def reporte_turnos():
    print("\n--- Reporte de Turnos ---")
    medicos = TurnoRepository.medicos_con_mas_turnos()
    for medico in medicos:
        print(f"Médico ID: {medico.id_medico}, Turnos: {medico.cantidad_turnos}")

def cancelacion_turnos():
    print("\n--- Cancelación de Turnos ---")
    id_medico = input("ID del Médico: ")
    fecha_inicio = input("Fecha de Inicio (AAAA-MM-DD): ")
    fecha_fin = input("Fecha de Fin (AAAA-MM-DD): ")
    turnos = TurnoRepository.obtener_turnos_por_medico_y_fecha(id_medico, fecha_inicio, fecha_fin)
    for turno in turnos:
        TurnoRepository.cancelar_turno(turno.id)
    print("Turnos cancelados con éxito.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            gestion_pacientes()
        elif opcion == '2':
            gestion_doctores()
        elif opcion == '3':
            manejo_turnos()
        elif opcion == '4':
            busquedas_avanzadas()
        elif opcion == '5':
            reporte_turnos()
        elif opcion == '6':
            cancelacion_turnos()
        elif opcion == '7':
            break
        else:
            print("Opción no válida.")

if __name__ == '__main__':
    with app.app_context():
        main()
