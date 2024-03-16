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
    def __init__(self, nombre: str, puntaje: int, ficha: str):
        self.nombre = nombre
        self.puntaje = puntaje
        self.ficha = ficha

class Casilla:
    def __init__(self):
        self.estado = 'vacio'  # los posibles estados son 'vacio', 'cruz' y 'circulo'

    def manejar_evento(self, evento):
        # Aquí se manejarían los eventos relacionados a la casilla
        pass

class Tablero:
    def __init__(self, N):
        self.N = N
        self.casillas = [[[Casilla() for _ in range(N)] for _ in range(N)] for _ in range(N)]

    def verificar_estado(self):
        # Aquí se verificaría el estado del tablero y las posibles líneas
        pass

    def actualizar_datos(self):
        # Aquí se actualizarían los datos del juego
        pass

class DatosDelJuego:
    def __init__(self, jugador1: Jugador, jugador2: Jugador, tablero: Tablero):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.turno_actual = jugador1  # El jugador1 comienza
        self.tablero = tablero

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
