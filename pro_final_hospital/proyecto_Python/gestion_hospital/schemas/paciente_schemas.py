from marshmallow import Schema, fields

class PacienteSchema(Schema):
    id_paciente = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    apellido = fields.Str(required=True)
    edad = fields.Int()
    direccion = fields.Str()
    telefono = fields.Str()
    email = fields.Email()
