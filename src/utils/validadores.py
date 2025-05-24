import os
import json
from typing import Any


# TODO: Añadir opción para exportar listados a CSV o PDF desde el menú de listados.
# TODO: Incluir opción de filtrar empleados por cargo o rango salarial.
# TODO: Permitir edición de contratos existentes (actualizar fechas o salario).
# TODO: Añadir opción de ver el historial de cambios de un empleado o contrato.
# TODO: Implementar autenticación básica para acceso restringido a ciertas funciones.
# TODO: Añadir opción de realizar copias de seguridad y restauración de datos.
# TODO: Incluir ayuda interactiva o guía de uso desde el menú principal.
# TODO: Permitir la eliminación masiva de empleados o contratos seleccionados.
# TODO: Añadir opción para enviar notificaciones por email sobre contratos próximos a vencer.


class GestorJSON:
    """
    Clase para gestionar la lectura y escritura de archivos JSON.
    Permite cambiar fácilmente el backend de almacenamiento en el futuro.

    Args:
        ruta (str): Ruta relativa al archivo JSON a gestionar.

    Métodos:
        leer(): Lee y devuelve el contenido del archivo JSON.
        escribir(datos): Escribe los datos en el archivo JSON.
    """
    def __init__(self, ruta: str):
        self.ruta = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../', ruta))

    def leer(self) -> Any:
        """
        Lee y devuelve el contenido del archivo JSON.

        Returns:
            Any: Datos leídos del archivo, o None si no existe o está vacío.
        """
        if not os.path.exists(self.ruta):
            return None
        with open(self.ruta, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return None

    def escribir(self, datos: Any):
        """
        Escribe los datos en el archivo JSON.

        Args:
            datos (Any): Datos a guardar en el archivo (debe ser serializable a JSON).
        """
        with open(self.ruta, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
