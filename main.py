import tkinter as tk
import typing
##Líneas 141, 197,210, 29 y 48
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
    def __init__(self, lienzo: tk.Canvas):
        self.lienzo: tk.Canvas = lienzo
        self.lado: int = 30
        self.x: int = self.lado + self.lado*(1/3)+self.lado+10
        self.y: int = 10
        self.estado = 'vacío'  # Puede ser 'vacío', 'cruz' o 'círculo'
        self.dibujar_casilla()
##Acá traté de implementar lo que está en la línea 210
    def dibujar_casilla(self):
        self.casilla = self.lienzo.create_rectangle(self.x,self.y,self.x+self.lado,self.y+self.lado,fill="light grey")
        self.etiqueta = tk.Label(self.lienzo, text=str(self.estado), font=("Arial",self.lado))
        ##Lo del click y el cursor
    
    def colocar_ficha(self, ficha):
        if self.estado == 'vacío':
            self.estado = ficha
            return True
        else:
            return False  # La casilla ya está ocupada

class Tablero:
    def __init__(self, dimension, root: tk.Tk):
        self.root = root
        self.lienzo = tk.Canvas(root)
        self.dimension: int = dimension
        self.casillas = [[[Casilla(self.lienzo) for _ in range(dimension)] for _ in range(dimension)] for _ in range(dimension)]
## Acá está lo que te comentaba de la función dibujar tablero
    def dibujar_tablero(self,root):
        for i in self.casillas:
            for j in i:
                for k in j:
                    k.dibujar_casilla()

    def verificar_lineas(self):
        # Aquí se implementaría la lógica para verificar si hay líneas ganadoras en el tablero
        pass

class DatosDelJuego:
    def __init__(self, jugador1, jugador2, dimension, root: tk.Tk):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.turno_actual = jugador1
        self.tablero = Tablero(dimension, root)

    def cambiar_turno(self):
        if self.turno_actual == self.jugador1:
            self.turno_actual = self.jugador2
        else:
            self.turno_actual = self.jugador1

# Ejemplo de uso
jugador1 = Jugador("Jugador 1", 'cruz')
jugador2 = Jugador("Jugador 2", 'círculo')

#datos_juego = DatosDelJuego(jugador1, jugador2, 3)

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

#------------------------------------------------------------

# Función para mostrar el menú pre-juego
def mostrar_menu_pre_juego():

    # Función para manejar la selección del usuario en el menú pre-juego
    def seleccionar_opcion(opcion):
        if opcion == "Regresar":
            root.destroy()  # Cerrar la ventana del menú pre-juego
            mostrar_menu_principal()  # Mostrar nuevamente el menú principal
        elif opcion == "Iniciar":
            root.destroy()  # Cerrar la ventana del menú pre-juego
            jugar(datos_juego)  # Ir al inicio del juego

    # Crear la ventana del menú pre-juego
    root = tk.Tk()
    root.title("Menu Pre-Juego")

    # Etiqueta para mostrar el título del menú pre-juego
    titulo_label = tk.Label(root, text="Menu Pre-Juego", font=("Helvetica", 18))
    titulo_label.pack(pady=10)
    
    # Etiqueta con el mensaje ingresar nombre del jugador 1
    ingresar_nombre_jugador1 = tk.Label(root, text="Ingrese nombre del jugador 1", font=("Helvetica", 10))
    ingresar_nombre_jugador1.pack(pady=5)
    
    # Entrada de texto para ingresar nombre del jugador 1
    ingresar_nombre_jugador1 = tk.Entry(root)
    ingresar_nombre_jugador1.pack()

  ##  Esta es la parte que no me guarda el nombre
    nombre1: str = ingresar_nombre_jugador1.get()
    jugador1: Jugador = Jugador(nombre1,"cruz")
    

    # Etiqueta con el mensaje ingresar nombre del jugador 2
    ingresar_nombre_jugador2 = tk.Label(root, text="Ingrese nombre del jugador 2", font=("Helvetica", 10))
    ingresar_nombre_jugador2.pack(pady=5)
    
    # Entrada de texto para ingresar nombre del jugador 2
    ingresar_nombre_jugador2 = tk.Entry(root)
    ingresar_nombre_jugador2.pack(pady=10)
  ##Acá tampoco guarda el nombre
    jugador2: Jugador = Jugador(ingresar_nombre_jugador2.get(),"círculo")

    # Etiqueta con el mensaje ingresar dimensión del tablero
    ingresar_nombre_jugador2 = tk.Label(root, text="Ingrese dimensión del tablero", font=("Helvetica", 10))
    ingresar_nombre_jugador2.pack(pady=5)
    
    # Entrada de texto para ingresar la dimension del tablero
    ingresar_dimension_tablero = tk.Entry(root)
    ingresar_dimension_tablero.pack(pady=5)
    
    datos_juego = DatosDelJuego(jugador1, jugador2, 3, root)

    # Botón para iniciar el juego
    iniciar_button = tk.Button(root, text="Iniciar", command=lambda: seleccionar_opcion("Iniciar"))
    iniciar_button.pack()
    
    # Botón para regresar al menú principal
    regresar_button = tk.Button(root, text="Regresar", command=lambda: seleccionar_opcion("Regresar"))
    regresar_button.pack()

    # Ejecutar la ventana
    root.mainloop()

#------------------------------------------------------------

# Función para jugar
def jugar(datos_juego: DatosDelJuego):
    # Crear la ventana del juego
    root = tk.Tk()
    root.title("Juego")
    
    # Etiqueta para mostrar el título del juego
    titulo_label = tk.Label(root, text="Juego", font=("Helvetica", 18))
    titulo_label.pack(pady=10)

    # Etiqueta para mostrar el nombre y puntaje del jugador 1
    readyplayer1 = tk.Label(root, text="Nombre: "+datos_juego.jugador1.nombre+"\nPuntaje: "+str(datos_juego.jugador1.puntaje), font=("Helvetica", 10))
    readyplayer1.pack(side=tk.LEFT)

    # Etiqueta para mostrar el nombre y puntaje del jugador 2
    readyplayer2 = tk.Label(root, text="Nombre: "+datos_juego.jugador2.nombre+"\nPuntaje: "+str(datos_juego.jugador2.puntaje), font=("Helvetica", 10))
    readyplayer2.pack(side=tk.RIGHT)

  
  ## Acá estaba tratando de llamar a la función dibujar tablero
    canvas = tk.Canvas(root, width=300, height=450)
    datos_juego.tablero.dibujar_tablero(root)


    
    #lado: int = 30
    #dimension: int = datos_juego.tablero.dimension
    #canvas = tk.Canvas(root, width=lado*dimension*2, height=450)
    #canvas.pack()
    #x: int =  lado + lado*(1/3)
    #y: int = 10
  """
Aquí hay una funcion que crea un tablero modelo de NxNxN


    for i in range(dimension):
        for j in range(dimension):
            x = 30
            for k in range(dimension):
                canvas.create_rectangle(x,y,x+lado,y+lado,fill="light grey")
                x += lado+10
            if j != dimension-1:
                canvas.create_line(x-(lado+10)*dimension-10,y+(lado+5),x,y+(lado+5), width = 2, fill = "black")
                y += lado+10
            else:
                x -= 5
                for t in range(1,dimension):
                    canvas.create_line(x-(lado+10)*t,y-(lado+10)*(dimension-1)-10,x-(lado+10)*t,y+(lado+10), width = 3, fill = "black")   
                y += 2*lado
        
    
    # Ejecutar la ventana
    root.mainloop()
"""

#------------------------------------------------------------
    
# Función principal
def main():
    # Ejecutar el programa mostrando el menú principal
    mostrar_menu_principal()

# Llamada a la función main para iniciar el programa para ir probando
main()
