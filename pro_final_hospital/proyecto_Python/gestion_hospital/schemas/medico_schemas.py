from marshmallow import Schema, fields

class MedicoSchema(Schema):
    id_medico = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    apellido = fields.Str(required=True)
    especialidad = fields.Str()
    telefono = fields.Str()
    email = fields.Email()
