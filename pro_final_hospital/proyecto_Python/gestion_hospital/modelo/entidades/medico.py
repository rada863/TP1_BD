from app import db

class Medico(db.Model):
    __tablename__ = 'medico'
    id_medico = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    especialidad = db.Column(db.String(50))
    telefono = db.Column(db.String(20))
    email = db.Column(db.String(100))
