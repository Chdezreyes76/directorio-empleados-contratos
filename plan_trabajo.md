## PLAN DE TRABAJO

### OBJETIVOS

Se desarrollará una aplicación en Python que administre un directorio de empleados y sus contratos laborales utilizando archivos JSON como almacenamiento de datos. La aplicación debe permitir:

-	Agregar, actualizar y eliminar empleados.
-	Registrar contratos laborales asociados a los empleados.
-	Consultar información de empleados y sus contratos.
-	Generar reportes básicos (por ejemplo, empleados con contratos vencidos).
-	Guardar y recuperar información de un archivo JSON.
-	Implementar pruebas unitarias sobre las funcionalidades clave.

### PAUTAS DE ELABORACION

#### Módulo gestor_empleados.py

- Maneja la creación, actualización, eliminación y consulta de empleados.

- guarda la información en **empleados.json.**

#### Módulo gestor_contratos.py

- Maneja la asociación de contratos laborales a empleados.
- Permite filtrar contratos activos y vencidos.


#### Módulo main.py

- Ofrece una interfaz de terminal para interactuar con el sistema.

#### Ejemplo de empleados.json

```JSON
{
    "empleados": [
        {
            "id": 1,
            "nombre": "Carlos Pérez",
            "cargo": "Desarrollador",
            "contratos": [
                {
                    "id_contrato": 101,
                    "fecha_inicio": "2023-02-15",
                    "fecha_fin": "2024-02-15",
                    "salario": 3500
                }
            ]
        }
    ]
}
```

#### Implementación del gestor_empleados.py
 - Carga y guarda los datos en empleados.json.
 - Métodos clave:
    - agregar_empleado(nombre, cargo) → dict
    - eliminar_empleado(id) → bool
    - buscar_empleado(id) → dict

#### Implementacion del gestor contratos_py
 - Permite agregar y actualizar contratos de empleados.
 - Métodos clave:
    - asociar_contrato(id_empleado, fecha_inicio, fecha_fin, salario) → dict
    - listar_contratos_vencidos() → list
    
### Implementacion del main.py
 - Ofrece un menú interactivo por terminal con opciones para gestionar empleados y contratos.

#### Pruebas del proyecto
Implementacion de pruebas unitarias con la libreria pytest.
 - Probar que se agregan empleados correctamente.
 - Probar que se eliminan empleados correctamente.
 - Probar la busqueda de empleados.
 - Probar que un empleado tiene contratos asociados.
  
#### Documentacion del proyecto

El README.md incluira:
 - Objetivos del proyecto.
 - Instrucciones de instalación y uso.
 - Ejemplos de uso.
