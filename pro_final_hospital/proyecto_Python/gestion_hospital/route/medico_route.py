from flask import Blueprint, request, jsonify
from modelo.repositorio.medico_repositorio import MedicoRepository
from schemas.medico_schemas import MedicoSchema

medico_bp = Blueprint('medico_bp', __name__)
medico_schema = MedicoSchema()
medicos_schema = MedicoSchema(many=True)

@medico_bp.route('/medicos', methods=['GET'])
def obtener_medicos():
    medicos = MedicoRepository.obtener_todos_los_medicos()
    return medicos_schema.jsonify(medicos)

@medico_bp.route('/medicos/<int:id_medico>', methods=['GET'])
def obtener_medico(id_medico):
    medico = MedicoRepository.obtener_medico_por_id(id_medico)
    if medico:
        return medico_schema.jsonify(medico)
    return jsonify({"message": "Médico no encontrado"}), 404

@medico_bp.route('/medicos', methods=['POST'])
def crear_medico():
    datos = request.json
    nuevo_medico = MedicoRepository.crear_medico(
        datos['nombre'], datos['apellido'], datos.get('especialidad'),
        datos.get('telefono'), datos.get('email')
    )
    return medico_schema.jsonify(nuevo_medico), 201

@medico_bp.route('/medicos/<int:id_medico>', methods=['PUT'])
def actualizar_medico(id_medico):
    datos = request.json
    medico_actualizado = MedicoRepository.actualizar_medico(
        id_medico, datos['nombre'], datos['apellido'], datos.get('especialidad'),
        datos.get('telefono'), datos.get('email')
    )
    if medico_actualizado:
        return medico_schema.jsonify(medico_actualizado)
    return jsonify({"message": "Médico no encontrado"}), 404

@medico_bp.route('/medicos/<int:id_medico>', methods=['DELETE'])
def eliminar_medico(id_medico):
    if MedicoRepository.eliminar_medico(id_medico):
        return jsonify({"message": "Médico eliminado con éxito"}), 200
    return jsonify({"message": "Médico no encontrado"}), 404
