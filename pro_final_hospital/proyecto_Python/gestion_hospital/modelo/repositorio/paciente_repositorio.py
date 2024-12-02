from modelo.entidades.paciente import Paciente
from app import db

class PacienteRepository:
    @staticmethod
    def crear_paciente(nombre, apellido, edad, direccion, telefono, email):
        paciente = Paciente(nombre=nombre, apellido=apellido, edad=edad, direccion=direccion, telefono=telefono, email=email)
        db.session.add(paciente)
        db.session.commit()
        return paciente

    @staticmethod
    def obtener_paciente_por_id(id_paciente):
        return Paciente.query.get(id_paciente)

    @staticmethod
    def actualizar_paciente(id_paciente, nombre, apellido, edad, direccion, telefono, email):
        paciente = Paciente.query.get(id_paciente)
        if paciente:
            paciente.nombre = nombre
            paciente.apellido = apellido
            paciente.edad = edad
            paciente.direccion = direccion
            paciente.telefono = telefono
            paciente.email = email
            db.session.commit()
            return paciente
        return None

    @staticmethod
    def eliminar_paciente(id_paciente):
        paciente = Paciente.query.get(id_paciente)
        if paciente:
            db.session.delete(paciente)
            db.session.commit()
            return True
        return False

    @staticmethod
    def obtener_todos_los_pacientes():
        return Paciente.query.all()
