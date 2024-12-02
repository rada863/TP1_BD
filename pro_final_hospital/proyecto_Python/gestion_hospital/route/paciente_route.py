from flask import Blueprint, request, jsonify
from modelo.repositorio.paciente_repositorio import PacienteRepository
from schemas.paciente_schemas import PacienteSchema

paciente_bp = Blueprint('paciente_bp', __name__)
paciente_schema = PacienteSchema()
pacientes_schema = PacienteSchema(many=True)

@paciente_bp.route('/pacientes', methods=['GET'])
def obtener_pacientes():
    pacientes = PacienteRepository.obtener_todos_los_pacientes()
    return pacientes_schema.jsonify(pacientes)

@paciente_bp.route('/pacientes/<int:id_paciente>', methods=['GET'])
def obtener_paciente(id_paciente):
    paciente = PacienteRepository.obtener_paciente_por_id(id_paciente)
    if paciente:
        return paciente_schema.jsonify(paciente)
    return jsonify({"message": "Paciente no encontrado"}), 404

@paciente_bp.route('/pacientes', methods=['POST'])
def crear_paciente():
    datos = request.json
    nuevo_paciente = PacienteRepository.crear_paciente(
        datos['nombre'], datos['apellido'], datos.get('edad'),
        datos.get('direccion'), datos.get('telefono'), datos.get('email')
    )
    return paciente_schema.jsonify(nuevo_paciente), 201

@paciente_bp.route('/pacientes/<int:id_paciente>', methods=['PUT'])
def actualizar_paciente(id_paciente):
    datos = request.json
    paciente_actualizado = PacienteRepository.actualizar_paciente(
        id_paciente, datos['nombre'], datos['apellido'], datos.get('edad'),
        datos.get('direccion'), datos.get('telefono'), datos.get('email')
    )
    if paciente_actualizado:
        return paciente_schema.jsonify(paciente_actualizado)
    return jsonify({"message": "Paciente no encontrado"}), 404

@paciente_bp.route('/pacientes/<int:id_paciente>', methods=['DELETE'])
def eliminar_paciente(id_paciente):
    if PacienteRepository.eliminar_paciente(id_paciente):
        return jsonify({"message": "Paciente eliminado con éxito"}), 200
    return jsonify({"message": "Paciente no encontrado"}), 404
