from flask import Blueprint, render_template, request, jsonify
from models.data_model import cargar_usuarios
import json
import os

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/pacientes', methods=['GET'])
def obtener_pacientes():
    # Leer los datos de los pacientes desde data.json
    usuarios = cargar_usuarios()
    return jsonify(usuarios)

@main_bp.route('/pacientes/<int:id>', methods=['GET'])
def obtener_paciente_por_id(id):
    # Leer los datos de los pacientes desde data.json
    usuarios = cargar_usuarios()
    
    # Buscar el paciente con el ID proporcionado
    paciente = next((p for p in usuarios if p['id'] == id), None)
    
    if paciente:
        return jsonify(paciente)
    else:
        return jsonify({"message": "Paciente no encontrado"}), 404

@main_bp.route('/pacientes/buscar', methods=['GET'])
def buscar_paciente():
    # Obtener los parámetros de búsqueda (id, nombre, cedula)
    nombre = request.args.get('nombre')
    cedula = request.args.get('cedula')
    
    # Leer los datos de los pacientes desde data.json
    usuarios = cargar_usuarios()

    # Filtrar por los parámetros disponibles
    if nombre:
        pacientes = [p for p in usuarios if nombre.lower() in p['nombre'].lower()]
        if pacientes:
            return jsonify(pacientes)
        else:
            return jsonify({"message": "No se encontraron pacientes con ese nombre"}), 404
    
    if cedula:
        pacientes = [p for p in usuarios if cedula in p['numero_identificacion']]
        if pacientes:
            return jsonify(pacientes)
        else:
            return jsonify({"message": "No se encontraron pacientes con esa cédula"}), 404

    return jsonify({"message": "Por favor, ingresa un criterio de búsqueda (id, nombre, o cedula)."}), 400

@main_bp.route('/pacientes', methods=['POST'])
def guardar_paciente():
    # Obtener los datos del paciente en formato JSON
    paciente_data = request.get_json()

    # Leer los datos actuales de los pacientes (desde data.json)
    usuarios = cargar_usuarios()

    # Agregar el nuevo paciente al listado
    nuevo_paciente = {
        "id": len(usuarios) + 1,  # Simplemente agregamos un ID secuencial
        "nombre": paciente_data['nombre'],
        "apellido": paciente_data['apellido'],
        "fecha_nacimiento": paciente_data['fecha_nacimiento'],
        "genero": paciente_data['genero'],
        "numero_identificacion": paciente_data['numero_identificacion']
    }
    
    usuarios.append(nuevo_paciente)

    # Guardar los datos actualizados en el archivo data.json
    ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'data.json')
    with open(ruta, 'w', encoding='utf-8') as archivo:
        json.dump(usuarios, archivo, ensure_ascii=False, indent=4)

    return jsonify({"message": "Paciente guardado correctamente", "paciente": nuevo_paciente}), 201

# Ruta para manejar el error 404 (página no encontrada)
@main_bp.app_errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404