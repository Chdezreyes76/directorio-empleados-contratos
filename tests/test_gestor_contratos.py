import pytest
from src.gestores.gestor_contratos import GestorContratos
from src.gestores.gestor_empleados import GestorEmpleados
import os
import shutil
import tempfile

@pytest.fixture(scope="function")
def gestor_contratos_tmp():
    temp_dir = tempfile.mkdtemp()
    ruta = os.path.join(temp_dir, "empleados_test.json")
    gestor_empleados = GestorEmpleados(ruta)
    gestor_contratos = GestorContratos(ruta)
    # Crear un empleado de prueba
    empleado = gestor_empleados.agregar_empleado("Test Contrato", "Dev")
    yield gestor_contratos, empleado.id
    shutil.rmtree(temp_dir)

def test_asociar_contrato(gestor_contratos_tmp):
    gestor_contratos, id_emp = gestor_contratos_tmp
    contrato = gestor_contratos.asociar_contrato(id_emp, "2024-01-01", "2025-01-01", 2000)
    assert contrato is not None
    contratos = gestor_contratos.listar_contratos_empleado(id_emp)
    assert len(contratos) == 1
    assert contratos[0].salario == 2000

def test_listar_contratos_vencidos(gestor_contratos_tmp):
    gestor_contratos, id_emp = gestor_contratos_tmp
    # Contrato vencido
    gestor_contratos.asociar_contrato(id_emp, "2022-01-01", "2023-01-01", 1000)
    # Contrato vigente
    gestor_contratos.asociar_contrato(id_emp, "2024-01-01", "2025-01-01", 2000)
    vencidos = gestor_contratos.listar_contratos_vencidos()
    # Comprobar que todos los contratos listados como vencidos tienen fecha_fin anterior a hoy
    from datetime import date, datetime
    hoy = date.today()
    for v in vencidos:
        fecha_fin = datetime.strptime(v["fecha_fin"], "%Y-%m-%d").date()
        assert fecha_fin < hoy, f"Contrato no vencido incluido: {v}"
    # Además, debe estar el contrato con salario 1000 (el vencido)
    assert any(v["salario"] == 1000 for v in vencidos)

def test_listar_contratos_empleado(gestor_contratos_tmp):
    gestor_contratos, id_emp = gestor_contratos_tmp
    gestor_contratos.asociar_contrato(id_emp, "2024-01-01", "2025-01-01", 2000)
    contratos = gestor_contratos.listar_contratos_empleado(id_emp)
    assert len(contratos) == 1
    assert contratos[0].fecha_inicio == "2024-01-01"
