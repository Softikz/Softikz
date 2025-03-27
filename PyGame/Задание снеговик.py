import random
import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Крестики-нолики")
        self.board = []
        self.buttons = []
        self.create_widgets()
        self.reset_board()
        
    def create_widgets(self):
        for i in range(9):
            button = tk.Button(self.window, text=" ", font=("Arial", 24), width=5, height=2,
                               command=lambda i=i: self.player_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)
    
    def reset_board(self):
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text=" ", state=tk.NORMAL)
    
    def player_move(self, index):
        if self.board[index] == " ":
            self.board[index] = "X"
            self.buttons[index].config(text="X", state=tk.DISABLED)
            if self.check_winner("X"):
                messagebox.showinfo("Игра окончена", "Вы победили!")
                self.reset_board()
            elif " " not in self.board:
                messagebox.showinfo("Игра окончена", "Ничья!")
                self.reset_board()
            else:
                self.computer_move()
    
    def computer_move(self):
        empty_cells = [i for i, val in enumerate(self.board) if val == " "]
        for marker in ["O", "X"]:
            for move in empty_cells:
                self.board[move] = marker
                if self.check_winner(marker):
                    self.board[move] = "O"
                    self.buttons[move].config(text="O", state=tk.DISABLED)
                    if marker == "O":
                        messagebox.showinfo("Игра окончена", "Компьютер победил!")
                        self.reset_board()
                    return
                self.board[move] = " "
        move = random.choice(empty_cells)
        self.board[move] = "O"
        self.buttons[move].config(text="O", state=tk.DISABLED)
        if self.check_winner("O"):
            messagebox.showinfo("Игра окончена", "Компьютер победил!")
            self.reset_board()
    
    def check_winner(self, marker):
        win_patterns = [(0,1,2), (3,4,5), (6,7,8),
                        (0,3,6), (1,4,7), (2,5,8),
                        (0,4,8), (2,4,6)]
        return any(self.board[a] == self.board[b] == self.board[c] == marker for a, b, c in win_patterns)
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
