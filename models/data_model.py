import json
import os

def cargar_usuarios():
    ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'data.json')
    with open(ruta, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)
