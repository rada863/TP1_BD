from app import db

class Turno(db.Model):
    __tablename__ = 'turno'
    id_turno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey('paciente.id_paciente'))
    id_medico = db.Column(db.Integer, db.ForeignKey('medico.id_medico'))
    fecha_hora = db.Column(db.DateTime)
    estado = db.Column(db.String(20))
