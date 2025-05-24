"""
Clase Menu para gestionar la interacción por terminal del sistema de empleados y contratos.

TODO: Añadir opción para exportar listados a CSV o PDF desde el menú de listados.
TODO: Incluir opción de filtrar empleados por cargo o rango salarial.
TODO: Permitir edición de contratos existentes (actualizar fechas o salario).
TODO: Añadir opción de ver el historial de cambios de un empleado o contrato.
TODO: Implementar autenticación básica para acceso restringido a ciertas funciones.
TODO: Añadir opción de realizar copias de seguridad y restauración de datos.
TODO: Incluir ayuda interactiva o guía de uso desde el menú principal.
TODO: Permitir la eliminación masiva de empleados o contratos seleccionados.
TODO: Añadir opción para enviar notificaciones por email sobre contratos próximos a vencer.
"""
from src.gestores.gestor_empleados import GestorEmpleados
from src.gestores.gestor_contratos import GestorContratos

class Menu:
    def __init__(self):
        self.gestor_empleados = GestorEmpleados()
        self.gestor_contratos = GestorContratos()

    def mostrar(self):
        while True:
            print("\n===== MENÚ PRINCIPAL =====")
            print("1. Gestión de empleados")
            print("2. Gestión de contratos")
            print("3. Listados y consultas")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.menu_empleados()
            elif opcion == "2":
                self.menu_contratos()
            elif opcion == "3":
                self.menu_listados()
            elif opcion == "4":
                print("Saliendo del sistema. ¡Hasta pronto!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def menu_empleados(self):
        while True:
            print("\n--- Gestión de empleados ---")
            print("1. Agregar empleado")
            print("2. Eliminar empleado")
            print("3. Buscar empleado por ID")
            print("4. Buscar empleado por nombre")
            print("5. Actualizar empleado")
            print("6. Listar empleados ordenados por nombre")
            print("7. Contar empleados (total y vigentes)")
            print("8. Volver al menú principal")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.agregar_empleado()
            elif opcion == "2":
                self.eliminar_empleado()
            elif opcion == "3":
                self.buscar_empleado_id()
            elif opcion == "4":
                self.buscar_empleado_nombre()
            elif opcion == "5":
                self.actualizar_empleado()
            elif opcion == "6":
                self.listar_empleados()
            elif opcion == "7":
                self.contar_empleados()
            elif opcion == "8":
                break
            else:
                print("Opción no válida.")

    def menu_contratos(self):
        while True:
            print("\n--- Gestión de contratos ---")
            print("1. Asociar contrato a empleado")
            print("2. Listar contratos de un empleado")
            print("3. Listar contratos vencidos")
            print("4. Volver al menú principal")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.asociar_contrato()
            elif opcion == "2":
                self.listar_contratos_empleado()
            elif opcion == "3":
                self.listar_contratos_vencidos()
            elif opcion == "4":
                break
            else:
                print("Opción no válida.")

    def menu_listados(self):
        while True:
            print("\n--- Listados y consultas ---")
            print("1. Listar todos los empleados")
            print("2. Listar empleados con contrato vigente")
            print("3. Listar contratos vencidos")
            print("4. Volver al menú principal")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.listar_empleados()
            elif opcion == "2":
                self.listar_empleados_vigentes()
            elif opcion == "3":
                self.listar_contratos_vencidos()
            elif opcion == "4":
                break
            else:
                print("Opción no válida.")

    # Métodos auxiliares para cada acción (implementación básica, se pueden mejorar)
    def agregar_empleado(self):
        print("\n--- Agregar empleado ---")
        nombre = input("Nombre: ")
        cargo = input("Cargo: ")
        try:
            empleado = self.gestor_empleados.agregar_empleado(nombre, cargo)
            print(f"Empleado agregado: {empleado.nombre} (ID: {empleado.id})")
        except Exception as e:
            print(f"Error: {e}")

    def eliminar_empleado(self):
        print("\n--- Eliminar empleado ---")
        try:
            id_emp = int(input("ID del empleado a eliminar: "))
            if self.gestor_empleados.eliminar_empleado(id_emp):
                print("Empleado eliminado correctamente.")
            else:
                print("No se encontró el empleado.")
        except Exception as e:
            print(f"Error: {e}")

    def buscar_empleado_id(self):
        print("\n--- Buscar empleado por ID ---")
        try:
            id_emp = int(input("ID del empleado: "))
            emp = self.gestor_empleados.buscar_empleado(id_emp)
            if emp:
                print(f"ID: {emp.id} | Nombre: {emp.nombre} | Cargo: {emp.cargo}")
            else:
                print("Empleado no encontrado.")
        except Exception as e:
            print(f"Error: {e}")

    def buscar_empleado_nombre(self):
        print("\n--- Buscar empleado por nombre ---")
        nombre = input("Nombre a buscar: ")
        empleados = self.gestor_empleados.buscar_empleados_por_nombre(nombre)
        if empleados:
            for emp in empleados:
                print(f"ID: {emp.id} | Nombre: {emp.nombre} | Cargo: {emp.cargo}")
        else:
            print("No se encontraron empleados con ese nombre.")

    def actualizar_empleado(self):
        print("\n--- Actualizar empleado ---")
        try:
            id_emp = int(input("ID del empleado: "))
            nombre = input("Nuevo nombre (dejar vacío para no cambiar): ")
            cargo = input("Nuevo cargo (dejar vacío para no cambiar): ")
            if self.gestor_empleados.actualizar_empleado(id_emp, nombre or None, cargo or None):
                print("Empleado actualizado correctamente.")
            else:
                print("No se encontró el empleado.")
        except Exception as e:
            print(f"Error: {e}")

    def listar_empleados(self):
        print("\n--- Listado de empleados ---")
        empleados = self.gestor_empleados.listar_empleados_ordenados()
        for emp in empleados:
            print(f"ID: {emp.id} | Nombre: {emp.nombre} | Cargo: {emp.cargo}")

    def contar_empleados(self):
        total = self.gestor_empleados.contar_empleados()
        vigentes = self.gestor_empleados.contar_empleados(solo_vigentes=True)
        print(f"Total de empleados: {total}")
        print(f"Empleados con contrato vigente: {vigentes}")

    def asociar_contrato(self):
        print("\n--- Asociar contrato a empleado ---")
        try:
            id_emp = int(input("ID del empleado: "))
            fecha_inicio = input("Fecha inicio (YYYY-MM-DD): ")
            fecha_fin = input("Fecha fin (YYYY-MM-DD): ")
            salario = float(input("Salario: "))
            contrato = self.gestor_contratos.asociar_contrato(id_emp, fecha_inicio, fecha_fin, salario)
            print(f"Contrato asociado (ID: {contrato.id_contrato})")
        except Exception as e:
            print(f"Error: {e}")

    def listar_contratos_empleado(self):
        print("\n--- Contratos de un empleado ---")
        try:
            id_emp = int(input("ID del empleado: "))
            contratos = self.gestor_contratos.listar_contratos_empleado(id_emp)
            if contratos:
                for c in contratos:
                    print(f"ID: {c.id_contrato} | Inicio: {c.fecha_inicio} | Fin: {c.fecha_fin} | Salario: {c.salario}")
            else:
                print("No se encontraron contratos para ese empleado.")
        except Exception as e:
            print(f"Error: {e}")

    def listar_contratos_vencidos(self):
        print("\n--- Contratos vencidos ---")
        vencidos = self.gestor_contratos.listar_contratos_vencidos()
        if vencidos:
            for v in vencidos:
                print(f"Empleado: {v['empleado']} | ID Contrato: {v['id_contrato']} | Fin: {v['fecha_fin']} | Salario: {v['salario']}")
        else:
            print("No hay contratos vencidos.")

    def listar_empleados_vigentes(self):
        print("\n--- Empleados con contrato vigente ---")
        empleados = self.gestor_empleados.cargar_empleados()
        from datetime import datetime
        hoy = datetime.now().date()
        for emp in empleados:
            for c in emp.contratos:
                try:
                    if "fecha_fin" in c and datetime.strptime(c["fecha_fin"], "%Y-%m-%d").date() >= hoy:
                        print(f"ID: {emp.id} | Nombre: {emp.nombre} | Cargo: {emp.cargo}")
                        break
                except Exception:
                    continue
