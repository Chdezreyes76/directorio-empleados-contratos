import pytest
from src.gestores.gestor_empleados import GestorEmpleados
import os
import shutil
import tempfile

@pytest.fixture(scope="function")
def gestor_empleados_tmp():
    # Crear un archivo temporal para pruebas
    temp_dir = tempfile.mkdtemp()
    ruta = os.path.join(temp_dir, "empleados_test.json")
    gestor = GestorEmpleados(ruta)
    yield gestor
    shutil.rmtree(temp_dir)

def test_agregar_empleado(gestor_empleados_tmp):
    empleado = gestor_empleados_tmp.agregar_empleado("Juan Pérez", "Tester")
    assert empleado.nombre == "Juan Pérez"
    assert empleado.cargo == "Tester"
    empleados = gestor_empleados_tmp.cargar_empleados()
    assert any(e.nombre == "Juan Pérez" for e in empleados)

def test_eliminar_empleado(gestor_empleados_tmp):
    emp = gestor_empleados_tmp.agregar_empleado("Ana Test", "QA")
    assert gestor_empleados_tmp.eliminar_empleado(emp.id) is True
    assert gestor_empleados_tmp.buscar_empleado(emp.id) is None

def test_buscar_empleado(gestor_empleados_tmp):
    emp = gestor_empleados_tmp.agregar_empleado("Carlos Busqueda", "Dev")
    encontrado = gestor_empleados_tmp.buscar_empleado(emp.id)
    assert encontrado is not None
    assert encontrado.nombre == "Carlos Busqueda"

def test_actualizar_empleado(gestor_empleados_tmp):
    emp = gestor_empleados_tmp.agregar_empleado("Nombre Antiguo", "Cargo Antiguo")
    actualizado = gestor_empleados_tmp.actualizar_empleado(emp.id, nombre="Nombre Nuevo", cargo="Cargo Nuevo")
    assert actualizado is True
    emp_actualizado = gestor_empleados_tmp.buscar_empleado(emp.id)
    assert emp_actualizado.nombre == "Nombre Nuevo"
    assert emp_actualizado.cargo == "Cargo Nuevo"

def test_buscar_empleados_por_nombre(gestor_empleados_tmp):
    gestor_empleados_tmp.agregar_empleado("Pedro Prueba", "Dev")
    gestor_empleados_tmp.agregar_empleado("Pedro Segundo", "QA")
    resultados = gestor_empleados_tmp.buscar_empleados_por_nombre("Pedro")
    assert len(resultados) == 2

def test_listar_empleados_ordenados(gestor_empleados_tmp):
    gestor_empleados_tmp.agregar_empleado("Zeta", "Dev")
    gestor_empleados_tmp.agregar_empleado("Alfa", "QA")
    empleados = gestor_empleados_tmp.listar_empleados_ordenados()
    assert empleados[0].nombre == "Alfa"
    assert empleados[-1].nombre == "Zeta"

def test_contar_empleados(gestor_empleados_tmp):
    gestor_empleados_tmp.agregar_empleado("Uno", "Dev")
    gestor_empleados_tmp.agregar_empleado("Dos", "QA")
    total = gestor_empleados_tmp.contar_empleados()
    assert total == 2
