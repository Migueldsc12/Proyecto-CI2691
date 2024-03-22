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
    def __init__(self, lienzo: tk.Canvas, lado: int, x: int, y: int,i: int,j: int):
        self.estado = 'X'  # Puede ser 'vacío', 'cruz' o 'círculo'
        self.lienzo: tk.Canvas = lienzo
        self.lado: int = lado
        self.x: int = x
        self.y: int = y
        self.i: int = i
        self.j: int = j
        self.dibujar_casilla()

    def dibujar_casilla(self):
        self.celda = self.lienzo.create_rectangle(self.x,self.y,self.x+self.lado,self.y+self.lado, fill = "light grey")
        #if empezo:
        #    canvas.tag_bind(celda, "<Button-1>", lambda:self.colocar_ficha())
        
        #self.state = tk.Label(self.lienzo, text="X", font=("Arial",self.lado-15), background = "light grey")
        #self.state.grid(row=self.i,column=self.j)


    def colocar_ficha(self, ficha):
        if self.estado == 'vacío':
            self.estado = ficha
            return True
        else:
            return False  # La casilla ya está ocupada

class Tablero:
    def __init__(self, dimension, lienzo: tk.Canvas):
        self.lienzo: tk.Canvas = lienzo
        self.dimension = dimension
        #self.empezo_juego: bool = empezo
        #if empezo:
            
        #else:
        self.dibujar_tablero()

    def dibujar_tablero(self):
        y: int = 10
        for i in range(self.dimension):
            x: int = 30
            for j in range(self.dimension):
                kasilla: Casilla = Casilla(self.lienzo,30,x,y,i,j)
                x+=35
            y+=35

            #Casilla(self.tabla,30,x,y) for _ in range(dimension)] for _ in range(dimension)]]
        

    #def dibujar_tablero(self):
        
        #for i in self.casillas:
         #   x: int = 10
          #  for j in i:
           #     kasilla: Casilla = Casilla(lienzo,30,x,y)
            #    x+=35
            #y+=35
            
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
    root = tk.Tk()
    root.title("Inicia el juego")
    root.geometry("400x400")
    lienzo = tk.Canvas(root, width=50*longitud_tablero, height=50*longitud_tablero)
    
    tablero: Tablero = Tablero(longitud_tablero,lienzo)
    tablero=[[" " for _ in range(longitud_tablero)] for _ in range(longitud_tablero)]

    # Inicializar los datos de los jugadores
    jugador1 = {"nombre": nombre_jugador1, "turno": 1, "ficha": "X", "puntuacion": 0}
    jugador2 = {"nombre": nombre_jugador2, "turno": 2, "ficha": "O", "puntuacion": 0}

    player1: Jugador = Jugador(nombre_jugador1,"X")
    player2: Jugador = Jugador(nombre_jugador2,"O")

    jugador1_label = tk.Label(root, text="Jugador 1: "+player1.nombre+"\nPuntaje: "+str(player1.puntaje))
    jugador1_label.grid(row=0,column=0)
    jugador2_label = tk.Label(root, text="Jugador 2: "+player2.nombre+"\nPuntaje: "+str(player2.puntaje))
    jugador2_label.grid(row=0,column=2)


    lienzo.grid(row=1,column=1)
    ###Falta ponerle que al terminar juego se resetean los datos
    terminar_button = tk.Button(root, text="Terminar Juego", command=lambda: [root.destroy(),mostrar_menu_principal()])
    terminar_button.grid(row=2,column=1)
    #Retornar el tablero y los datos de los jugadores
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
    jugar_button = tk.Button(root, text="Jugar", command=lambda: [root.destroy(),mostrar_menu_pre_juego(root)])
    salir_button = tk.Button(root, text="Salir", command=root.destroy)

    jugar_button.pack(pady=20)
    salir_button.pack(pady=20)

    root.mainloop()

def cambiar_size(size: tk.Label, x: int, pabajo: bool):
    if pabajo:
        if int(size.cget("text")) > 3:
            size.configure(text=str(int(size.cget("text"))+x))
    else:
        size.configure(text=str(int(size.cget("text"))+x))

def revision_de_nombres(jugador1_entry: tk.Entry, jugador2_entry: tk.Entry, root: tk.Tk, size: str, error_label: tk.Label):
    if jugador1_entry.get() == jugador2_entry.get():
        error_label.configure(text="Los nombres de los jugadores no pueden ser iguales.")
    elif jugador1_entry.get() == "":
        error_label.configure(text="Ingresa un nombre para el jugador 1.")
    elif jugador2_entry.get() == "":
        error_label.configure(text="Ingresa un nombre para el jugador 2.")
    else:
        seleccionar_opcion(jugador1_entry.get(), jugador2_entry.get(), size, root)
    

# Mostrar menú pre-juego
def mostrar_menu_pre_juego(root):
    root = tk.Tk()
    root.title("Configuración de juego")
    root.geometry("400x300")

    # Agregar etiquetas y entradas para nombres de jugadores y longitud del tablero
    jugador1_label = tk.Label(root, text="Nombre Jugador 1:")
    jugador1_entry = tk.Entry(root)
    jugador2_label = tk.Label(root, text="Nombre Jugador 2:")
    jugador2_entry = tk.Entry(root)
    longitud_label = tk.Label(root, text="Longitud del tablero:")
    size_label = tk.Label(root, text="3", font= 14)
    subir_size_button = tk.Button(root,text="↑", font=10, command=lambda: cambiar_size(size_label,1,False))
    bajar_size_button = tk.Button(root,text="↓", font=10, command=lambda: cambiar_size(size_label,-1,True))
    longitud_entry = tk.Entry(root)

    jugador1_label.pack()
    jugador1_entry.pack()
    jugador2_label.pack()
    jugador2_entry.pack()
    longitud_label.pack()
    subir_size_button.pack()
    size_label.pack()
    bajar_size_button.pack()

    error_label = tk.Label(root, text="", font=20)
    error_label.pack()
    
    # Agregar botones para regresar e iniciar
    regresar_button = tk.Button(root, text="Regresar", command=lambda: [root.destroy(),mostrar_menu_principal()])
    iniciar_button = tk.Button(root, text="Iniciar", command=lambda: revision_de_nombres(jugador1_entry,jugador2_entry, root ,size_label.cget("text"),error_label))

    iniciar_button.pack(pady=10)
    regresar_button.pack(pady=5)
    

    root.mainloop()

# Seleccionar opción
def seleccionar_opcion(jugador1, jugador2, longitud_tablero, root):
    tablero, jugador1_data, jugador2_data = inicializar_juego(jugador1, jugador2, int(longitud_tablero))
    #ganador: bool = False
    #while !ganador:
        
            
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

