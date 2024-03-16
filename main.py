import tkinter as tk
import typing

"""
Proyecto CI-2691 N en raya 3D

Integrantes:
- Miguel Salomon (19-10274)
- Gabriel De Ornelas (15-10377) 

"""

# ESTRUCTURAS DE DATOS PRINCIPALES

class Jugador:
    def __init__(self, nombre, ficha):
        self.nombre = nombre
        self.puntaje = 0
        self.ficha = ficha

class Casilla:
    def __init__(self):
        self.estado = 'vacío'  # Puede ser 'vacío', 'cruz' o 'círculo'

    def colocar_ficha(self, ficha):
        if self.estado == 'vacío':
            self.estado = ficha
            return True
        else:
            return False  # La casilla ya está ocupada

class Tablero:
    def __init__(self, dimension):
        self.dimension = dimension
        self.casillas = [[[Casilla() for _ in range(dimension)] for _ in range(dimension)] for _ in range(dimension)]

    def verificar_lineas(self):
        # Aquí se implementaría la lógica para verificar si hay líneas ganadoras en el tablero
        pass

class DatosDelJuego:
    def __init__(self, jugador1, jugador2, dimension):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.turno_actual = jugador1
        self.tablero = Tablero(dimension)

    def cambiar_turno(self):
        if self.turno_actual == self.jugador1:
            self.turno_actual = self.jugador2
        else:
            self.turno_actual = self.jugador1

# Ejemplo de uso
jugador1 = Jugador("Jugador 1", 'cruz')
jugador2 = Jugador("Jugador 2", 'círculo')

datos_juego = DatosDelJuego(jugador1, jugador2, 3)

#------------------------------------------------------------

# Función para mostrar el menú principal
def mostrar_menu_principal():

    # Función para manejar la selección del usuario en el menú principal
    def seleccionar_opcion(opcion):
        if opcion == "Jugar":
            root.destroy()  # Cerrar la ventana del menú principal
            mostrar_menu_pre_juego()

        elif opcion == "Salir":
            root.destroy()  # Cerrar la ventana y finalizar el programa

    # Crear la ventana principal
    root = tk.Tk()
    root.title("Menú Principal")

    # Etiqueta para mostrar el título del menú
    titulo_label = tk.Label(root, text="Menú Principal", font=("Helvetica", 18))
    titulo_label.pack(pady=10)

    # Botón para mostrar el menú pre-juego
    mostrar_menu_pre_juego_button = tk.Button(root, text="Jugar", command=lambda: seleccionar_opcion("Jugar"))
    mostrar_menu_pre_juego_button.pack()

    # Botón para salir del programa
    salir_button = tk.Button(root, text="Salir", command=lambda: seleccionar_opcion("Salir"))
    salir_button.pack()

    # Ejecutar la ventana
    root.mainloop()

# Función para mostrar el menú pre-juego
def mostrar_menu_pre_juego():

    # Función para manejar la selección del usuario en el menú pre-juego
    def seleccionar_opcion(opcion):
        if opcion == "Regresar":
            root.destroy()  # Cerrar la ventana del menú pre-juego
            mostrar_menu_principal()  # Mostrar nuevamente el menú principal

    # Crear la ventana del menú pre-juego
    root = tk.Tk()
    root.title("Menu Pre-Juego")

    # Etiqueta para mostrar el título del menú pre-juego
    titulo_label = tk.Label(root, text="Menu Pre-Juego", font=("Helvetica", 18))
    titulo_label.pack(pady=10)

    # Botón para regresar al menú principal
    regresar_button = tk.Button(root, text="Regresar", command=lambda: seleccionar_opcion("Regresar"))
    regresar_button.pack()

    # Ejecutar la ventana
    root.mainloop()

# Función principal
def main():
    # Ejecutar el programa mostrando el menú principal
    mostrar_menu_principal()

# Llamada a la función main para iniciar el programa para ir probando
main()






#ESTRUCTURA DE CODIGO A SEGUIR

# def main():
"""
Funcion principal del juego
"""

#     salir = False

#     while(True):
#         mostrar_menu_principal()
#         obtener_opcion_del_usuario()

#         if(salir == True):
#             salir()

#         else:
#             mostrar_menu_prejuego():
#             obtener_opcion_del_usuario()

#         if(obtener_opcion_del_usuario() == 2):
#             regresar()
        
#         else:
#             iniciar_juego()

#         while(True):
#             mostrar_tablero()
#             obtener_accion_del_usuario()

#             if(obtener_accion_del_usuario() == 2):
#                 break

#             llenar_casilla()

#             procesar_tablero()

#             if(hay_linea()):
#                 sumar_punto()
#                 reiniciar_tablero()
#                 intercambiar_turno()
