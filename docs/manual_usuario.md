# Manual de Usuario

## Introducción
Este sistema permite gestionar empleados y contratos laborales desde una interfaz de menú en terminal. Está diseñado para ser fácil de usar, seguro y ampliable.

---

## Inicio rápido
1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Ejecuta el sistema:
   ```bash
   python main.py
   ```

---

## Menú principal
Al iniciar el sistema verás un menú con las siguientes opciones:

1. Gestión de empleados
2. Gestión de contratos
3. Listados y consultas
4. Salir

Selecciona la opción deseada introduciendo el número correspondiente.

---

## Funciones principales y ejemplos

### 1. Gestión de empleados
- **Agregar empleado:** Introduce nombre y cargo. El sistema asigna un ID automáticamente.
- **Eliminar empleado:** Ingresa el ID del empleado a eliminar.
- **Buscar empleado:** Puedes buscar por ID o por nombre.
- **Actualizar empleado:** Modifica nombre o cargo de un empleado existente.
- **Listar empleados:** Muestra todos los empleados ordenados por nombre.
- **Contar empleados:** Muestra el número total de empleados registrados.

**Ejemplo:**
```
Seleccione una opción: 1
1. Agregar empleado
2. Eliminar empleado
...
Seleccione una opción: 1
Nombre: Juan Pérez
Cargo: Desarrollador
Empleado agregado con ID 3
```

### 2. Gestión de contratos
- **Asociar contrato:** Selecciona un empleado, indica fechas y salario.
- **Listar contratos de un empleado:** Muestra todos los contratos asociados a un empleado.
- **Listar contratos vencidos:** Muestra contratos cuya fecha de fin ya ha pasado.

**Ejemplo:**
```
Seleccione una opción: 2
1. Asociar contrato
2. Listar contratos de un empleado
3. Listar contratos vencidos
...
```

### 3. Listados y consultas
- **Listar empleados por nombre, cargo o vigencia de contrato.**
- **Resúmenes:** Número de empleados con contrato vigente, etc.

---

## Consejos de uso
- Utiliza siempre el menú para navegar y realizar acciones.
- Los datos se guardan automáticamente tras cada operación.
- Si introduces un dato incorrecto, el sistema mostrará un mensaje de error y te permitirá reintentarlo.

---

## Referencia rápida de funciones
| Función                        | Descripción                                      |
|-------------------------------|--------------------------------------------------|
| Agregar empleado              | Alta de nuevo empleado                           |
| Eliminar empleado             | Baja de empleado por ID                          |
| Buscar empleado               | Búsqueda por ID o nombre                         |
| Actualizar empleado           | Modificación de datos de empleado                |
| Listar empleados              | Muestra todos los empleados ordenados            |
| Contar empleados              | Total de empleados registrados                   |
| Asociar contrato              | Añade contrato a un empleado                     |
| Listar contratos de empleado  | Muestra contratos de un empleado                 |
| Listar contratos vencidos     | Muestra contratos cuya fecha de fin ya pasó      |

---

## Soporte
Para dudas o incidencias, consulta el README.md o contacta con el responsable del proyecto.
