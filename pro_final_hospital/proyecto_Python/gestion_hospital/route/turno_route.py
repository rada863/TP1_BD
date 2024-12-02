from flask import Blueprint, request, jsonify
from modelo.repositorio.turno_repositorio import TurnoRepository
from schemas.turno_schemas import TurnoSchema

turno_bp = Blueprint('turno_bp', __name__)
turno_schema = TurnoSchema()
turnos_schema = TurnoSchema(many=True)

@turno_bp.route('/turnos', methods=['GET'])
def obtener_turnos():
    turnos = TurnoRepository.obtener_todos_los_turnos()
    return turnos_schema.jsonify(turnos)

@turno_bp.route('/turnos/<int:id_turno>', methods=['GET'])
def obtener_turno(id_turno):
    turno = TurnoRepository.obtener_turno_por_id(id_turno)
    if turno:
        return turno_schema.jsonify(turno)
    return jsonify({"message": "Turno no encontrado"}), 404

@turno_bp.route('/turnos', methods=['POST'])
def crear_turno():
    datos = request.json
    nuevo_turno = TurnoRepository.crear_turno(
        datos['id_paciente'], datos['id_medico'],
        datos['fecha_hora'], datos.get('estado', 'Programado')
    )
    return turno_schema.jsonify(nuevo_turno), 201

@turno_bp.route('/turnos/<int:id_turno>', methods=['PUT'])
def actualizar_turno(id_turno):
    datos = request.json
    turno_actualizado = TurnoRepository.actualizar_turno(
        id_turno, datos['id_paciente'], datos['id_medico'],
        datos['fecha_hora'], datos.get('estado', 'Programado')
    )
    if turno_actualizado:
        return turno_schema.jsonify(turno_actualizado)
    return jsonify({"message": "Turno no encontrado"}), 404

@turno_bp.route('/turnos/<int:id_turno>', methods=['DELETE'])
def eliminar_turno(id_turno):
    if TurnoRepository.eliminar_turno(id_turno):
        return jsonify({"message": "Turno eliminado con éxito"}), 200
    return jsonify({"message": "Turno no encontrado"}), 404
