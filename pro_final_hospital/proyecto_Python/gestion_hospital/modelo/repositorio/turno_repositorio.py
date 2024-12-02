from modelo.entidades.turno import Turno
from app import db

class TurnoRepository:
    @staticmethod
    def crear_turno(id_paciente, id_medico, fecha_hora, estado):
        turno = Turno(id_paciente=id_paciente, id_medico=id_medico, fecha_hora=fecha_hora, estado=estado)
        db.session.add(turno)
        db.session.commit()
        return turno

    @staticmethod
    def obtener_turno_por_id(id_turno):
        return Turno.query.get(id_turno)

    @staticmethod
    def actualizar_turno(id_turno, id_paciente, id_medico, fecha_hora, estado):
        turno = Turno.query.get(id_turno)
        if turno:
            turno.id_paciente = id_paciente
            turno.id_medico = id_medico
            turno.fecha_hora = fecha_hora
            turno.estado = estado
            db.session.commit()
            return turno
        return None

    @staticmethod
    def eliminar_turno(id_turno):
        turno = Turno.query.get(id_turno)
        if turno:
            db.session.delete(turno)
            db.session.commit()
            return True
        return False

    @staticmethod
    def obtener_todos_los_turnos():
        return Turno.query.all()
