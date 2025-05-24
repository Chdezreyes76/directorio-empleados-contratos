import os
import json
from typing import List, Optional, Dict, Any
from src.utils.validadores import GestorJSON

class Empleado:
    """
    Representa a un empleado del sistema.

    Args:
        id (int): Identificador único del empleado.
        nombre (str): Nombre completo del empleado.
        cargo (str): Cargo o puesto del empleado.
        contratos (list[dict], opcional): Lista de contratos asociados.

    Métodos:
        from_dict(data): Crea un Empleado a partir de un diccionario.
        to_dict(): Convierte el empleado a un diccionario serializable.
    """
    def __init__(self, id: int, nombre: str, cargo: str, contratos: Optional[List[Dict[str, Any]]] = None):
        self.id = id
        self.nombre = nombre
        self.cargo = cargo
        self.contratos = contratos if contratos is not None else []

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Empleado':
        """
        Crea un objeto Empleado a partir de un diccionario.

        Args:
            data (dict): Diccionario con las claves 'id', 'nombre', 'cargo', 'contratos'.
        Returns:
            Empleado: Instancia creada a partir del diccionario.
        """
        return Empleado(
            id=data.get('id'),
            nombre=data.get('nombre'),
            cargo=data.get('cargo'),
            contratos=data.get('contratos', [])
        )

    def to_dict(self) -> Dict[str, Any]:
        """
        Convierte el empleado a un diccionario serializable para almacenamiento.

        Returns:
            dict: Representación serializable del empleado.
        """
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cargo": self.cargo,
            "contratos": self.contratos
        }

class GestorEmpleados:
    """
    Gestiona el alta, baja, búsqueda, actualización y listado de empleados.
    Utiliza un archivo JSON como almacenamiento persistente.

    Args:
        ruta_json (str): Ruta al archivo JSON de empleados.
    """
    def __init__(self, ruta_json: str = "data/empleados.json"):
        self.gestor_json = GestorJSON(ruta_json)

    def cargar_empleados(self) -> List[Empleado]:
        """
        Carga todos los empleados desde el archivo JSON.

        Returns:
            list[Empleado]: Lista de empleados cargados.
        """
        data = self.gestor_json.leer()
        if not data or "empleados" not in data:
            return []
        return [Empleado.from_dict(e) for e in data["empleados"]]

    def guardar_empleados(self, empleados: List[Empleado]):
        """
        Guarda la lista de empleados en el archivo JSON.

        Args:
            empleados (list[Empleado]): Lista de empleados a guardar.
        """
        self.gestor_json.escribir({"empleados": [e.to_dict() for e in empleados]})

    def agregar_empleado(self, nombre: str, cargo: str) -> Optional[Empleado]:
        """
        Agrega un nuevo empleado al sistema.

        Args:
            nombre (str): Nombre del empleado.
            cargo (str): Cargo del empleado.
        Returns:
            Empleado o None: El empleado creado, o None si falla la validación.
        Raises:
            ValueError: Si nombre o cargo están vacíos.
        """
        if not nombre or not cargo:
            raise ValueError("El nombre y el cargo son obligatorios.")
        empleados = self.cargar_empleados()
        nuevo_id = max([e.id for e in empleados], default=0) + 1
        nuevo = Empleado(nuevo_id, nombre, cargo)
        empleados.append(nuevo)
        self.guardar_empleados(empleados)
        return nuevo

    def eliminar_empleado(self, empleado_id: int) -> bool:
        """
        Elimina un empleado por su ID.

        Args:
            empleado_id (int): ID del empleado a eliminar.
        Returns:
            bool: True si se eliminó, False si no existe.
        """
        empleados = self.cargar_empleados()
        nuevos = [e for e in empleados if e.id != empleado_id]
        if len(nuevos) == len(empleados):
            return False
        self.guardar_empleados(nuevos)
        return True

    def buscar_empleado(self, empleado_id: int) -> Optional[Empleado]:
        """
        Busca un empleado por su ID.

        Args:
            empleado_id (int): ID del empleado a buscar.
        Returns:
            Empleado o None: El empleado encontrado, o None si no existe.
        """
        empleados = self.cargar_empleados()
        for e in empleados:
            if e.id == empleado_id:
                return e
        return None

    def buscar_empleados_por_nombre(self, nombre: str) -> List[Empleado]:
        """
        Busca empleados cuyo nombre contenga el texto indicado (no sensible a mayúsculas).

        Args:
            nombre (str): Texto a buscar en el nombre.
        Returns:
            list[Empleado]: Lista de empleados que coinciden.
        """
        empleados = self.cargar_empleados()
        return [e for e in empleados if nombre.lower() in e.nombre.lower()]

    def actualizar_empleado(self, empleado_id: int, nombre: Optional[str] = None, cargo: Optional[str] = None) -> bool:
        """
        Actualiza el nombre y/o cargo de un empleado existente.

        Args:
            empleado_id (int): ID del empleado a actualizar.
            nombre (str, opcional): Nuevo nombre.
            cargo (str, opcional): Nuevo cargo.
        Returns:
            bool: True si se actualizó, False si no existe.
        """
        empleados = self.cargar_empleados()
        actualizado = False
        for e in empleados:
            if e.id == empleado_id:
                if nombre:
                    e.nombre = nombre
                if cargo:
                    e.cargo = cargo
                actualizado = True
                break
        if actualizado:
            self.guardar_empleados(empleados)
        return actualizado

    def listar_empleados_ordenados(self) -> List[Empleado]:
        """
        Devuelve la lista de empleados ordenada alfabéticamente por nombre.

        Returns:
            list[Empleado]: Lista ordenada de empleados.
        """
        return sorted(self.cargar_empleados(), key=lambda e: e.nombre)

    def contar_empleados(self, solo_vigentes: bool = False) -> int:
        """
        Cuenta el número total de empleados, o solo los que tienen contrato vigente.

        Args:
            solo_vigentes (bool): Si True, solo cuenta empleados con contrato vigente.
        Returns:
            int: Número de empleados.
        """
        empleados = self.cargar_empleados()
        if not solo_vigentes:
            return len(empleados)
        # Considera vigente si tiene al menos un contrato con fecha_fin en el futuro
        from datetime import datetime
        hoy = datetime.now().date()
        vigentes = 0
        for e in empleados:
            for c in e.contratos:
                try:
                    if "fecha_fin" in c and datetime.strptime(c["fecha_fin"], "%Y-%m-%d").date() >= hoy:
                        vigentes += 1
                        break
                except Exception:
                    continue
        return vigentes
