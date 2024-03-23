
"""
Cosas que faltan: comentarios, tipos de variables
"""

import tkinter as tk
from tkinter import messagebox
from typing import List

"""
Proyecto - CI2691 - N en Raya

Integrantes:

Miguel Salomon - 1910274
Gabriel de Ornela - 1510377

"""

class Juego:
    def __init__(self, n, player1, player2):

        self.n = n

        self.board = [['' for _ in range(n)] for _ in range(n)]

        self.players = { 'X': player1, 'O': player2 }

        self.scores = { 'X': 0, 'O': 0 }

        self.current_player = 'X'
        
        self.window = tk.Tk()
        self.window.title('N en Raya')

        self.current_player_label = tk.Label(self.window, text=f'Turno de {self.players[self.current_player]} ({self.current_player})')
        self.current_player_label.pack()

        self.canvas = tk.Canvas(self.window, width=n*100, height=n*100, bg='white')
        self.canvas.pack()

        self.player1_frame = tk.Frame(self.window)
        self.player1_frame.pack(side=tk.LEFT)

        self.player1_label = tk.Label(self.player1_frame, text=f'{player1}')
        self.player1_label.pack()

        self.score1_puntaje = tk.Label(self.player1_frame, text=f'Puntaje: {self.scores["X"]}')
        self.score1_puntaje.pack()

        self.player2_frame = tk.Frame(self.window)
        self.player2_frame.pack(side=tk.RIGHT)

        self.player2_label = tk.Label(self.player2_frame, text=f'{player2}')
        self.player2_label.pack()

        self.score2_puntaje = tk.Label(self.player2_frame, text=f'Puntaje: {self.scores["O"]}')
        self.score2_puntaje.pack()

        self.quit_button = tk.Button(self.window, text='Salir', command=self.volver_al_menu)
        self.quit_button.pack()

        self.dibujar_tablero()  # Dibujar el tablero inicialmente
        self.actualizar_puntaje()  # Actualizar los puntajes

    def volver_al_menu(self):

        self.window.destroy()
        menu_principal = MenuPrincipal()
        menu_principal.window.mainloop()

    def reiniciar_juego(self):

        self.board = [['' for _ in range(self.n)] for _ in range(self.n)]
        self.current_player = 'X'

        # Guarda los puntajes actuales
        score_X = self.scores['X']
        score_O = self.scores['O']

        # Intercambia los nombres de los jugadores
        self.players['X'], self.players['O'] = self.players['O'], self.players['X']

        # Intercambia los puntajes
        self.scores['X'] = score_O
        self.scores['O'] = score_X

        # Actualiza las etiquetas de los jugadores
        self.current_player_label.config(text=f'Turno de {self.players[self.current_player]} ({self.current_player})')

        self.dibujar_tablero()
        self.actualizar_puntaje() # Actualizar las etiquetas de los jugadores con los nuevos nombres

    def actualizar_puntaje(self):

        self.player1_label.config(text=f'{self.players["X"]}')
        self.player2_label.config(text=f'{self.players["O"]}')
        self.score1_puntaje['text'] = f'Puntaje: {self.scores["X"]}'
        self.score2_puntaje['text'] = f'Puntaje: {self.scores["O"]}'  # Dibujar el tablero inicialmente

    def dibujar_tablero(self):

        for i in range(self.n):
            for j in range(self.n):
                self.canvas.create_rectangle(i*100, j*100, i*100+100, j*100+100, fill='white')

                if self.board[i][j] != '':
                    color = 'red' if self.board[i][j] == 'X' else 'blue'
                    self.canvas.create_text(i*100+50, j*100+50, text=self.board[i][j], font=('Arial', 50), fill=color)

    def click(self, event):

        x = event.x // 100
        y = event.y // 100

        if self.board[x][y] == '':
            self.board[x][y] = self.current_player
            self.dibujar_tablero()

            if self.procesar_tablero():
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

    def procesar_tablero(self):

        for i in range(self.n):

            # Revisar si hay una fila o columna completa
            if all(self.board[i][j] == self.current_player for j in range(self.n)) or all(self.board[j][i] == self.current_player for j in range(self.n)):
                return True
        
        # Revisar si hay una diagonal completa
        if all(self.board[i][i] == self.current_player for i in range(self.n)) or all(self.board[i][self.n-i-1] == self.current_player for i in range(self.n)):
            return True
        
        return False
    
    def empate(self):

    # Comprueba si todas las celdas del tablero están llenas
        for row in self.board:

            for cell in row:
            
                if cell == '':
                    return False  # Si hay una celda vacía, no es un empate

        # Si todas las celdas están llenas y no hay un ganador, es un empate
        return not self.procesar_tablero()

    def jugar(self):

        self.canvas.bind('<Button-1>', self.click)
        self.window.mainloop()


class VentanaInicio:

    def __init__(self):

        self.window = tk.Tk()
        self.window.title('Inicio del juego')

        # Establecer el tamaño de la ventana a 500x500
        self.window.geometry('500x500')

        tk.Label(self.window, text='Nombre del Jugador 1:').pack()
        self.player1_entry = tk.Entry(self.window)
        self.player1_entry.pack()
        
        tk.Label(self.window, text='Nombre del Jugador 2:').pack()
        self.player2_entry = tk.Entry(self.window)
        self.player2_entry.pack()
        
        tk.Label(self.window, text='Dimensiones del tablero:').pack()
        self.board_size_entry = tk.Entry(self.window)
        self.board_size_entry.pack()
        
        tk.Button(self.window, text='Iniciar juego', command=self.iniciar_juego).pack()
        tk.Button(self.window, text='Regresar', command=self.volver_al_menu).pack()

    def volver_al_menu(self):
        
        self.window.destroy()
        menu_principal = MenuPrincipal()
        menu_principal.window.mainloop()

    def iniciar_juego(self):

        player1 = self.player1_entry.get()
        player2 = self.player2_entry.get()

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

        tk.Label(self.window, text='Bienvenido al juego!').pack()
        tk.Button(self.window, text='Jugar', command=self.abrir_ventana_inicio).pack()
        tk.Button(self.window, text='Salir', command=self.window.destroy).pack()

    def abrir_ventana_inicio(self):

        self.window.destroy()
        ventana_inicio = VentanaInicio()
        ventana_inicio.window.mainloop()


# Crear y ejecutar la ventana de menú principal
menu_principal = MenuPrincipal()
menu_principal.window.mainloop()
