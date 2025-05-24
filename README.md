# Sistema de Directorio de Empleados y Contratos

## Datos del autor
**Autor:** Carlos Hernández Reyes
**Fecha:** 2025/05/24
**Curso:** Programa Avanzado en Inteligencia Artificial para Programar
**Institución:** UNIR (Universidad Internacional de La Rioja)


## Objetivo del proyecto
Este sistema permite gestionar empleados y sus contratos laborales de forma sencilla, escalable y segura. Incluye funcionalidades para alta, baja, búsqueda, actualización y listado de empleados, así como la gestión de contratos asociados, control de vencimientos y consultas avanzadas. El sistema está diseñado para ser modular, fácilmente ampliable y con pruebas unitarias.

## Estructura del proyecto
```
directorio_empleados/
├── src/                    # Código fuente principal
│   ├── gestores/           # Módulos de gestión de empleados y contratos
│   └── utils/              # Utilidades y validadores
├── data/                   # Datos persistentes (empleados.json)
├── tests/                  # Pruebas unitarias
├── docs/                   # Documentación y manual de usuario
├── main.py                 # Punto de entrada principal
├── README.md               # Este archivo
└── requirements.txt        # Dependencias
```

## Instalación
1. Clona el repositorio o descarga el código fuente.
2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta el sistema:
   ```bash
   python main.py
   ```

## Uso básico
- El sistema se maneja mediante un menú interactivo por terminal.
- Permite gestionar empleados (alta, baja, búsqueda, actualización, listados).
- Permite asociar contratos a empleados, consultar contratos vencidos y listados avanzados.
- Todas las operaciones están validadas y documentadas.

## Ejecución de pruebas
Para ejecutar las pruebas unitarias:
```bash
pytest tests/
```

## Créditos y licencia
Desarrollado como actividad académica para UNIR. Uso educativo.

---
Para más detalles, consulta el manual de usuario en `docs/manual_usuario.md`.
