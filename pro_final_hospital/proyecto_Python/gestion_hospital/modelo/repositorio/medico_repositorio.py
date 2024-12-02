from modelo.entidades.medico import Medico
from app import db

class MedicoRepository:
    @staticmethod
    def crear_medico(nombre, apellido, especialidad, telefono, email):
        medico = Medico(nombre=nombre, apellido=apellido, especialidad=especialidad, telefono=telefono, email=email)
        db.session.add(medico)
        db.session.commit()
        return medico

    @staticmethod
    def obtener_medico_por_id(id_medico):
        return Medico.query.get(id_medico)

    @staticmethod
    def actualizar_medico(id_medico, nombre, apellido, especialidad, telefono, email):
        medico = Medico.query.get(id_medico)
        if medico:
            medico.nombre = nombre
            medico.apellido = apellido
            medico.especialidad = especialidad
            medico.telefono = telefono
            medico.email = email
            db.session.commit()
            return medico
        return None

    @staticmethod
    def eliminar_medico(id_medico):
        medico = Medico.query.get(id_medico)
        if medico:
            db.session.delete(medico)
            db.session.commit()
            return True
        return False

    @staticmethod
    def obtener_todos_los_medicos():
        return Medico.query.all()
