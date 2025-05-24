import os
import json
from typing import Any

class GestorJSON:
    """
    Clase para gestionar la lectura y escritura de archivos JSON.
    Permite cambiar fácilmente el backend de almacenamiento en el futuro.
    """
    def __init__(self, ruta: str):
        self.ruta = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../', ruta))

    def leer(self) -> Any:
        """Lee y devuelve el contenido del archivo JSON. Si no existe, devuelve None."""
        if not os.path.exists(self.ruta):
            return None
        with open(self.ruta, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return None

    def escribir(self, datos: Any):
        """Escribe los datos en el archivo JSON."""
        with open(self.ruta, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
