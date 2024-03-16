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

import tkinter as tk

def mostrar_menu_principal():
    """
    Funcion que muestra el menu principal del juego
    """

def mostrar_menu_principal():
    # Función para iniciar el juego
    def jugar():
        print("Iniciar juego")

    # Función para salir del programa
    def salir():
        print("Salir del juego")
        root.destroy()

    # Crear la ventana principal
    root = tk.Tk()
    root.title("Menú Principal")

    # Establecer el tamaño de la ventana
    root.geometry("300x200")  # Anchura x Altura

    # Botón para iniciar el juego
    jugar_button = tk.Button(root, text="Jugar", command=jugar)
    jugar_button.pack(pady=10)

    # Botón para salir del programa
    salir_button = tk.Button(root, text="Salir", command=salir)
    salir_button.pack(pady=10)

    # Ejecutar la ventana
    root.mainloop()

# Ejemplo de uso
mostrar_menu_principal()




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
