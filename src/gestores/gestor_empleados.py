import os
import json
from typing import List, Optional, Dict, Any
from src.utils.validadores import GestorJSON

class Empleado:
    """
    Clase que representa a un empleado y sus métodos asociados.
    """
    def __init__(self, id: int, nombre: str, cargo: str, contratos: Optional[List[Dict[str, Any]]] = None):
        self.id = id
        self.nombre = nombre
        self.cargo = cargo
        self.contratos = contratos if contratos is not None else []

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Empleado':
        return Empleado(
            id=data.get('id'),
            nombre=data.get('nombre'),
            cargo=data.get('cargo'),
            contratos=data.get('contratos', [])
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cargo": self.cargo,
            "contratos": self.contratos
        }

class GestorEmpleados:
    """
    Clase para gestionar empleados, con validaciones y manejo de excepciones.
    """
    def __init__(self, ruta_json: str = "data/empleados.json"):
        self.gestor_json = GestorJSON(ruta_json)

    def cargar_empleados(self) -> List[Empleado]:
        data = self.gestor_json.leer()
        if not data or "empleados" not in data:
            return []
        return [Empleado.from_dict(e) for e in data["empleados"]]

    def guardar_empleados(self, empleados: List[Empleado]):
        self.gestor_json.escribir({"empleados": [e.to_dict() for e in empleados]})

    def agregar_empleado(self, nombre: str, cargo: str) -> Optional[Empleado]:
        if not nombre or not cargo:
            raise ValueError("El nombre y el cargo son obligatorios.")
        empleados = self.cargar_empleados()
        nuevo_id = max([e.id for e in empleados], default=0) + 1
        nuevo = Empleado(nuevo_id, nombre, cargo)
        empleados.append(nuevo)
        self.guardar_empleados(empleados)
        return nuevo

    def eliminar_empleado(self, empleado_id: int) -> bool:
        empleados = self.cargar_empleados()
        nuevos = [e for e in empleados if e.id != empleado_id]
        if len(nuevos) == len(empleados):
            return False
        self.guardar_empleados(nuevos)
        return True

    def buscar_empleado(self, empleado_id: int) -> Optional[Empleado]:
        empleados = self.cargar_empleados()
        for e in empleados:
            if e.id == empleado_id:
                return e
        return None

    def buscar_empleados_por_nombre(self, nombre: str) -> List[Empleado]:
        empleados = self.cargar_empleados()
        return [e for e in empleados if nombre.lower() in e.nombre.lower()]

    def actualizar_empleado(self, empleado_id: int, nombre: Optional[str] = None, cargo: Optional[str] = None) -> bool:
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
        return sorted(self.cargar_empleados(), key=lambda e: e.nombre)

    def contar_empleados(self, solo_vigentes: bool = False) -> int:
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
