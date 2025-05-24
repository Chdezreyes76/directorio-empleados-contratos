"""
Punto de entrada principal del sistema de gestión de empleados y contratos.
Lanza el menú interactivo por terminal.
"""
from src.utils.menu import Menu

if __name__ == "__main__":
    menu = Menu()
    menu.mostrar()
