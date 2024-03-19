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
        self.casillas = [[[Casilla() for _ in range(dimension)] for _ in range(dimension)]]

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

#---------------------------------------------------------------------------------------------------------------------------
# Función para inicializar el juego
def inicializar_juego(nombre_jugador1, nombre_jugador2, longitud_tablero):
    # Crear el tablero N x N
    tablero = [[" " for _ in range(longitud_tablero)] for _ in range(longitud_tablero)]

    # Inicializar los datos de los jugadores
    jugador1 = {"nombre": nombre_jugador1, "turno": 1, "ficha": "X", "puntuacion": 0}
    jugador2 = {"nombre": nombre_jugador2, "turno": 2, "ficha": "O", "puntuacion": 0}

    # Retornar el tablero y los datos de los jugadores
    return tablero, jugador1, jugador2

# Función principal
def main():
    # Mostrar el menú principal
    mostrar_menu_principal()

# Mostrar menú principal
def mostrar_menu_principal():
    root = tk.Tk()
    root.title("N en Raya 3D")
    root.geometry("400x200")

    # Agregar botones para jugar y salir
    jugar_button = tk.Button(root, text="Jugar", command=lambda: mostrar_menu_pre_juego(root))
    salir_button = tk.Button(root, text="Salir", command=root.quit)

    jugar_button.pack(pady=20)
    salir_button.pack(pady=20)

    root.mainloop()

# Mostrar menú pre-juego
def mostrar_menu_pre_juego(root):
    root.destroy()  # Cerrar ventana anterior
    root = tk.Tk()
    root.title("Configuración de juego")
    root.geometry("400x300")

    # Agregar etiquetas y entradas para nombres de jugadores y longitud del tablero
    jugador1_label = tk.Label(root, text="Nombre Jugador 1:")
    jugador1_entry = tk.Entry(root)
    jugador2_label = tk.Label(root, text="Nombre Jugador 2:")
    jugador2_entry = tk.Entry(root)
    longitud_label = tk.Label(root, text="Longitud del tablero:")
    longitud_entry = tk.Entry(root)

    jugador1_label.pack()
    jugador1_entry.pack()
    jugador2_label.pack()
    jugador2_entry.pack()
    longitud_label.pack()
    longitud_entry.pack()

    # Agregar botones para regresar e iniciar
    regresar_button = tk.Button(root, text="Regresar", command=lambda: mostrar_menu_principal())
    iniciar_button = tk.Button(root, text="Iniciar", command=lambda: seleccionar_opcion(jugador1_entry.get(), jugador2_entry.get(), longitud_entry.get(), root))

    regresar_button.pack(pady=20)
    iniciar_button.pack(pady=20)

    root.mainloop()

# Seleccionar opción
def seleccionar_opcion(jugador1, jugador2, longitud_tablero, root):
    tablero, jugador1_data, jugador2_data = inicializar_juego(jugador1, jugador2, int(longitud_tablero))
    print("Juego iniciado con los siguientes datos:")
    print("Jugador 1:", jugador1_data)
    print("Jugador 2:", jugador2_data)
    print("Tablero:", tablero)
    root.destroy()

# Iniciar programa
if __name__ == "__main__":
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
