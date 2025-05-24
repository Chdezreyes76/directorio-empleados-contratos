import os
from datetime import datetime
from typing import List, Optional, Dict, Any
from src.utils.validadores import GestorJSON
from src.gestores.gestor_empleados import Empleado, GestorEmpleados

class Contrato:
    """
    Clase que representa un contrato laboral.
    """
    def __init__(self, id_contrato: int, fecha_inicio: str, fecha_fin: str, salario: float):
        self.id_contrato = id_contrato
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.salario = salario

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Contrato':
        return Contrato(
            id_contrato=data.get('id_contrato'),
            fecha_inicio=data.get('fecha_inicio'),
            fecha_fin=data.get('fecha_fin'),
            salario=data.get('salario')
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id_contrato": self.id_contrato,
            "fecha_inicio": self.fecha_inicio,
            "fecha_fin": self.fecha_fin,
            "salario": self.salario
        }

class GestorContratos:
    """
    Clase para gestionar contratos laborales asociados a empleados.
    """
    def __init__(self, ruta_json: str = "data/empleados.json"):
        self.gestor_empleados = GestorEmpleados(ruta_json)

    def asociar_contrato(self, id_empleado: int, fecha_inicio: str, fecha_fin: str, salario: float) -> Optional[Contrato]:
        empleados = self.gestor_empleados.cargar_empleados()
        empleado = next((e for e in empleados if e.id == id_empleado), None)
        if not empleado:
            raise ValueError("Empleado no encontrado.")
        # Validación de fechas y salario
        try:
            fi = datetime.strptime(fecha_inicio, "%Y-%m-%d")
            ff = datetime.strptime(fecha_fin, "%Y-%m-%d")
            if ff < fi:
                raise ValueError("La fecha de fin no puede ser anterior a la de inicio.")
            if salario <= 0:
                raise ValueError("El salario debe ser positivo.")
        except Exception as e:
            raise ValueError(f"Error en los datos del contrato: {e}")
        # Generar nuevo id_contrato
        todos_contratos = [c["id_contrato"] for emp in empleados for c in emp.contratos]
        nuevo_id = max(todos_contratos, default=100) + 1
        contrato = Contrato(nuevo_id, fecha_inicio, fecha_fin, salario)
        empleado.contratos.append(contrato.to_dict())
        self.gestor_empleados.guardar_empleados(empleados)
        return contrato

    def listar_contratos_vencidos(self) -> List[Dict[str, Any]]:
        empleados = self.gestor_empleados.cargar_empleados()
        hoy = datetime.now().date()
        vencidos = []
        for e in empleados:
            for c in e.contratos:
                try:
                    fecha_fin = datetime.strptime(c["fecha_fin"], "%Y-%m-%d").date()
                    if fecha_fin < hoy:
                        vencidos.append({
                            "empleado": e.nombre,
                            "id_empleado": e.id,
                            "id_contrato": c["id_contrato"],
                            "fecha_fin": c["fecha_fin"],
                            "salario": c["salario"]
                        })
                except Exception:
                    continue
        return vencidos

    def listar_contratos_empleado(self, id_empleado: int) -> List[Contrato]:
        empleado = self.gestor_empleados.buscar_empleado(id_empleado)
        if not empleado:
            return []
        return [Contrato.from_dict(c) for c in empleado.contratos]
