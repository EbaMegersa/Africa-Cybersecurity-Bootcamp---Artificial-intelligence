import tkinter as tk
import random

class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")
        self.root.geometry("400x200")
        
        # Game variables
        self.target_number = random.randint(1, 100)
        self.guess_count = 0
        
        # Create GUI elements
        self.title_label = tk.Label(root, text="Guess the Number (1 to 100)", font=("Helvetica", 14))
        self.title_label.pack(pady=10)
        
        self.instruction_label = tk.Label(root, text="Enter your guess:")
        self.instruction_label.pack()
        
        self.guess_entry = tk.Entry(root, width=10)
        self.guess_entry.pack(pady=5)
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=5)
        
        self.guess_button = tk.Button(root, text="Guess", command=self.check_guess)
        self.guess_button.pack()
        
        self.reset_button = tk.Button(root, text="Reset Game", command=self.reset_game)
        self.reset_button.pack(pady=10)
        
    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.guess_count += 1
            
            if guess < self.target_number:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.target_number:
                self.result_label.config(text="Too high! Try again.")
            else:
                self.result_label.config(text=f"Congratulations! You guessed it in {self.guess_count} tries.")
                self.guess_button.config(state=tk.DISABLED)
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")
        
    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.guess_count = 0
        self.result_label.config(text="")
        self.guess_entry.delete(0, tk.END)
        self.guess_button.config(state=tk.NORMAL)

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()
