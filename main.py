import tkinter as tk
from tkinter import messagebox
from typing import List

"""
Proyecto - CI2691 - N en Raya

Integrantes:

Miguel Salomon - 1910274
Gabriel De Ornelas - 1510377

"""

class Juego:
    def __init__(self, n, player1, player2):

        self.n: int = n
        
        if self.n > 3:
            self.size: int = 900//n
        
        else:
            self.size: int = 300

        self.board: List[List[List[int]]] = [[['' for _ in range(n)] for _ in range(n)] for _ in range(n)]

        self.players = { 'X': player1, 'O': player2 }

        self.scores = { 'X': 0, 'O': 0 }

        self.current_player: str = 'X'
        
        self.window = tk.Tk()
        self.window.title('N en Raya')
        self.window.geometry(str(n*self.size+300)+"x"+str(self.size+200))
        self.window.configure(bg = "midnight blue")

        self.current_player_label = tk.Label(self.window, text=f'Turno de {self.players[self.current_player]} ({self.current_player})', bg = "midnight blue", fg="white", font=("Stencil", 15))
        self.current_player_label.pack(pady=10)

        self.canvas = tk.Canvas(self.window, width=1000, height=self.size, bg = "midnight blue")
        self.canvas.pack()

        self.player1_frame = tk.Frame(self.window, bg = "midnight blue")
        self.player1_frame.pack(side=tk.LEFT)

        self.player1_label = tk.Label(self.player1_frame, text=f'{player1}',bg = "midnight blue", fg="white", font=("Stencil", 15))
        self.player1_label.pack()

        self.score1_puntaje = tk.Label(self.player1_frame, text=f'Puntaje: {self.scores["X"]}', bg = "midnight blue", fg="white", font=("Stencil", 15))
        self.score1_puntaje.pack()

        self.player2_frame = tk.Frame(self.window, bg = "midnight blue")
        self.player2_frame.pack(side=tk.RIGHT)

        self.player2_label = tk.Label(self.player2_frame, text=f'{player2}', bg = "midnight blue", fg="white", font=("Stencil", 15))
        self.player2_label.pack()

        self.score2_puntaje = tk.Label(self.player2_frame, text=f'Puntaje: {self.scores["O"]}', bg = "midnight blue", fg="white", font=("Stencil", 15))
        self.score2_puntaje.pack()

        self.quit_button = tk.Button(self.window, text='SALIR', font=("Bauhaus 93",13), bg="orange", borderwidth = 10, command=self.volver_al_menu)
        self.quit_button.pack(pady=30,ipadx=30, ipady=1)

        self.dibujar_tablero()  # Dibujar el tablero inicialmente
        self.actualizar_puntaje()  # Actualizar los puntajes

    def volver_al_menu(self) -> None:
        """
        Función que cierra la ventana actual y abre la ventana del menú principal

        args: None

        return: None
        """
        self.window.destroy()
        menu_principal = MenuPrincipal()
        menu_principal.window.mainloop()

    def reiniciar_juego(self) -> None:
        """
        Funcion que reinicia el juego, intercambiando los nombres de los jugadores y los puntajes

        args: None

        return: None
        """
        self.board: List[List[List[int]]] = [[['' for _ in range(self.n)] for _ in range(self.n)] for _ in range(self.n)]
        self.current_player: str = 'X'

        # Guarda los puntajes actuales
        score_X: int = self.scores['X']
        score_O: int = self.scores['O']

        # Intercambia los nombres de los jugadores
        self.players['X'], self.players['O'] = self.players['O'], self.players['X']

        # Intercambia los puntajes
        self.scores['X'] = score_O
        self.scores['O'] = score_X

        # Actualiza las etiquetas de los jugadores
        self.current_player_label.config(text=f'Turno de {self.players[self.current_player]} ({self.current_player})')

        self.dibujar_tablero()
        self.actualizar_puntaje() # Actualizar las etiquetas de los jugadores con los nuevos nombres

    def actualizar_puntaje(self) -> None:
        """
        Funcion que actualiza los puntajes de los jugadores en la ventana

        args: None

        return: None
        """
        self.player1_label.config(text=f'{self.players["X"]}')
        self.player2_label.config(text=f'{self.players["O"]}')
        self.score1_puntaje['text'] = f'Puntaje: {self.scores["X"]}'
        self.score2_puntaje['text'] = f'Puntaje: {self.scores["O"]}'

    def dibujar_tablero(self) -> None:
        """
        Funcion que dibuja el tablero en la ventana

        args: None

        return: Nones
        """
        lado: int = self.size // self.n
        tabla: int = 0

        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    self.canvas.create_rectangle(i*lado+tabla, j*lado, i*lado+lado+tabla, j*lado+lado, fill='white')

                    if self.board[k][i][j] != '':
                        color = 'red' if self.board[k][i][j] == 'X' else 'blue'
                        self.canvas.create_text(i*lado+tabla+lado//2, j*lado+lado//2, text=self.board[k][i][j], font=('Arial', lado//2), fill=color)
            tabla+=self.size+(100//(self.n-1))
            

    def click(self, event: tk.Event) -> None:
        """
        Funcion que se ejecuta al hacer click en una celda del tablero

        args: event: tk.Event

        return: None
        """
        z: int = event.x // (self.size + (100//(self.n-1)))
        x: int = (event.x % (self.size + (100//(self.n-1)))) // (self.size//self.n)
        y: int = event.y // (self.size//self.n)
            
        if self.board[z][x][y] == '':
            self.board[z][x][y] = self.current_player
            self.dibujar_tablero()
            
            if self.procesamiento_de_tablero(z,x,y):
                self.scores[self.current_player] += 1
                self.actualizar_puntaje()
                
                messagebox.showinfo('Ganador', f'El jugador {self.players[self.current_player]} gana!')
                self.reiniciar_juego()
                
            elif self.empate():
                messagebox.showinfo('Empate', 'El juego terminó en empate!')
                self.reiniciar_juego()
                
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.current_player_label.config(text=f'Turno de {self.players[self.current_player]} ({self.current_player})')

    def procesamiento_de_tablero(self, z: int, x: int, y: int) -> bool:
        """
        Función que revisa si hay un ganador luego del último movimiento
        """
        #Revisa si hay fila o culumna ganadora
        if all(self.board[z][x][k] == self.current_player for k in range(self.n)) or all(self.board[z][k][y] == self.current_player for k in range(self.n)):
            return True
        
        #Revisa si hay diagonal o diagonal inversa ganadora
        if all(self.board[z][k][k] == self.current_player for k in range(self.n)) or all(self.board[z][k][self.n-k-1] == self.current_player for k in range(self.n)):
            return True
        
        #Revisa si hay victoria intertablero
        if all(self.board[k][x][y] == self.current_player for k in range(self.n)):
            return True
        
        #Revisa si hay victoria de fila intertablero
        if all(self.board[k][x][k] == self.current_player for k in range(self.n)) or all(self.board[self.n-k-1][x][k] == self.current_player for k in range(self.n)):
            return True
        
        #Revisa si hay victoria de columna intertablero
        if all(self.board[k][k][y] == self.current_player for k in range(self.n)) or all(self.board[self.n-k-1][k][y] == self.current_player for k in range(self.n)):
            return True
        
        #Revisa si hay victoria de diagonal intertablero (desde [0][0][0] hasta [n-1][n-1][n-1] or desde [3][0][0] hasta [0][n-1][n-1])
        if all(self.board[k][k][k] == self.current_player for k in range(self.n)) or all(self.board[self.n-k-1][k][k] == self.current_player for k in range(self.n)):
            return True
        
        #Revisa si hay victoria de diagonal inversa intertablero (desde [0][n-1][0] hasta [n-1][0][n-1] or desde [n-1][n-1][0] hasta [0][0][n-1])
        if all(self.board[k][self.n-k-1][k] == self.current_player for k in range(self.n)) or all(self.board[k][k][self.n-k-1] == self.current_player for k in range(self.n)):
            return True
        return False
    
    def empate(self) -> bool:
        """
        Funcion que revisa si hay un empate en el tablero

        args: None

        return: bool
        """
    # Comprueba si todas las celdas del tablero están llenas
        for table in self.board:
            for row in table:
    
                for cell in row:
                
                    if cell == '':
                        return False  # Si hay una celda vacía, no es un empate

        # Si todas las celdas están llenas y no hay un ganador, es un empate
        return not self.procesamiento_de_tablero()

    def jugar(self) -> None:
        """
        Funcion que inicia el juego

        args: None

        return: None
        """
        self.canvas.bind('<Button-1>', self.click)
        self.window.mainloop()


class VentanaInicio:

    def __init__(self):

        self.window = tk.Tk()
        self.window.title('Inicio del juego')

        # Establecer el tamaño de la ventana a 500x500
        self.window.geometry('500x500')
        self.window.configure(bg = "midnight blue")

        # Circulo en el fondo
        self.lienzo=tk.Canvas(self.window,width=500,height=500,bg="midnight blue")
        self.lienzo.place(x=0,y=0)
        self.lienzo.create_oval(0,0,500,500, width = 50,outline="sky blue")

        tk.Label(self.window, text='INGRESE LOS DATOS DEL JUEGO', bg="midnight blue", fg="white", font=("bauhaus 93", 20)).pack(pady=30)
        
        tk.Label(self.window, text='Nombre del Jugador 1:',bg="midnight blue", fg="green yellow", font=("Stencil", 15)).pack(pady=5)
        self.player1_entry = tk.Entry(self.window, bg="sky blue", font=(15))
        self.player1_entry.pack(pady=5)
        
        tk.Label(self.window, text='Nombre del Jugador 2:', bg="midnight blue", fg="Orange", font=("Stencil", 15)).pack(pady=5)
        self.player2_entry = tk.Entry(self.window, bg="sky blue", font=(15))
        self.player2_entry.pack(pady=5)
        
        tk.Label(self.window, text='Dimensiones del tablero:', bg="Midnight blue", fg="white", font=("Stencil", 15)).pack(pady=5)
        self.board_size_entry = tk.Entry(self.window, bg="sky blue", font=(15))
        self.board_size_entry.pack(pady=5)
        
        tk.Button(self.window, text='INICIAR',font=("Bauhaus 93",10), bg="green yellow",borderwidth = 10, command=self.iniciar_juego).pack(pady=15,ipadx=50, ipady=5)
        tk.Button(self.window, text='REGRESAR',font=("Bauhaus 93",10), bg="orange",borderwidth = 10, command=self.volver_al_menu).pack(ipadx=43, ipady=5)

    def volver_al_menu(self) -> None:
        """
        Función que cierra la ventana actual y abre la ventana del menú principal

        args: None

        return: None
        """
        self.window.destroy()
        menu_principal = MenuPrincipal()
        menu_principal.window.mainloop()

    def iniciar_juego(self) -> None:
        """
        Función que inicia el juego con los datos ingresados por el usuario

        args: None

        return: None
        """
        player1: str = self.player1_entry.get()
        player2: str = self.player2_entry.get()

        # Verificar que los nombres de los jugadores no estén vacíos
        if not player1 or not player2:
            messagebox.showerror("Error", "Los nombres de los jugadores no pueden estar vacíos")
            return

        # Verificar que los nombres de los jugadores no sean iguales
        if player1 == player2:
            messagebox.showerror("Error", "Los nombres de los jugadores no pueden ser iguales")
            return

        # Verificar que la dimensión del tablero sea un número
        try:
            board_size = int(self.board_size_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Las dimensiones del tablero deben ser un número")
            return

        # Verificar que las dimensiones del tablero sean > 2
        if board_size <= 2:
            messagebox.showerror("Error", "Las dimensiones del tablero deben ser mayores a 2")
            return

        self.window.destroy()
        game = Juego(board_size, player1, player2)
        game.jugar()


class MenuPrincipal:

    def __init__(self):

        self.window = tk.Tk()
        self.window.title('Menú Principal')
        self.window.geometry('500x500')
        self.window.configure(bg = "midnight blue")

        #Cruz en el fondo
        self.lienzo=tk.Canvas(self.window,width=500,height=500,bg="midnight blue")
        self.lienzo.place(x=0,y=0)
        self.lienzo.create_line(0,0,500,500, width = 50,fill="sky blue")
        self.lienzo.create_line(0,500,500,0, width = 50,fill="sky blue")

        tk.Label(self.window, text='¡N EN RAYA 3D!', bg="midnight blue", fg="white", font=("Bauhaus 93", 40)).pack(pady=35)
        tk.Button(self.window, text='JUGAR', font=("Bauhaus 93",18), bg="green yellow",borderwidth = 10, command=self.abrir_ventana_inicio).pack(pady=18,ipadx=50, ipady=10)
        tk.Button(self.window, text='SALIR', font=("Bauhaus 93",18), bg="orange", borderwidth = 10, command=self.window.destroy).pack(pady= 5, ipadx=53, ipady=10)
        
        # integrantes
        nombres=tk.Label(self.window, text='INTEGRANTES', font=("Bauhaus 93",10), bg="white")
        nombres.pack(pady=32)
        names=tk.Label(self.window, text="", bg="midnight blue", fg="white", font=("Bauhaus 93", 10))
        names.pack()
        nombres.bind("<Enter>",lambda m :names.config(text="Miguel Salomon - 1910274\nGabriel De Ornelas - 1510377"))
        nombres.bind("<Leave>",lambda m :names.config(text=""))

    def abrir_ventana_inicio(self) -> None:
        """
        Función que cierra la ventana actual y abre la ventana de inicio del juego

        args: None

        return: None
        """
        self.window.destroy()
        ventana_inicio = VentanaInicio()
        ventana_inicio.window.mainloop()


# Crear y ejecutar la ventana de menú principal
menu_principal = MenuPrincipal()
menu_principal.window.mainloop()
