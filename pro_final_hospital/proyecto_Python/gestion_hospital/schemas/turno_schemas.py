from marshmallow import Schema, fields

class TurnoSchema(Schema):
    id_turno = fields.Int(dump_only=True)
    id_paciente = fields.Int(required=True)
    id_medico = fields.Int(required=True)
    fecha_hora = fields.DateTime(required=True)
    estado = fields.Str()
