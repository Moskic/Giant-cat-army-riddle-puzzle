import tkinter as tk
from tkinter import messagebox
import math

class PuzzleGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Puzzle Game")

        # Setting the initial window size
        self.window.geometry("520x200")

        self.value = 0
        self.visited_values = set()

        # Enlarging the font size for the label
        self.label = tk.Label(self.window, text=self.value, font=("Arial", 48))
        self.label.pack(pady=40)

        # Making the buttons larger
        self.button_5 = tk.Button(self.window, text="+5", command=self.add_5, font=("Arial", 20), width=8)
        self.button_5.pack(side=tk.LEFT, padx=20)

        self.button_7 = tk.Button(self.window, text="+7", command=self.add_7, font=("Arial", 20), width=8)
        self.button_7.pack(side=tk.LEFT, padx=20)

        self.button_sqrt = tk.Button(self.window, text="√", command=self.sqrt, font=("Arial", 20), width=8)
        self.button_sqrt.pack(side=tk.LEFT, padx=20)

    def add_5(self):
        self.update_value(self.value + 5)

    def add_7(self):
        self.update_value(self.value + 7)

    def sqrt(self):
        self.update_value(math.sqrt(self.value))

    def update_value(self, new_value):
        if new_value in self.visited_values:
            self.end_game("You outputted the same number twice!")
            return

        if new_value > 60:
            self.end_game("You outputted a number greater than 60!")
            return

        if new_value != int(new_value):
            self.end_game("You outputted a non-whole number!")
            return

        self.visited_values.add(new_value)
        self.value = int(new_value)
        self.label.config(text=str(self.value))
        
        if self.value in [2, 10, 14]:
            self.check_win()

    def check_win(self):
        if set([2, 10, 14]).issubset(self.visited_values):
            self.end_game("Congratulations! You solved the puzzle!")

    def end_game(self, message):
        messagebox.showinfo("Game Over", message)
        self.window.destroy()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = PuzzleGame()
    game.run()
