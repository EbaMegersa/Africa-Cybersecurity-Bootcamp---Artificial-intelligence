import tkinter as tk
from tkinter import messagebox
import random

# Initialize the main game window
root = tk.Tk()
root.title("Guess the Number Game")
root.geometry("400x300")

# Variables
number_to_guess = random.randint(1, 100)
attempts = 0

# Function to check the guess
def check_guess():
    global attempts
    global number_to_guess
    
    try:
        guess = int(entry.get())
        attempts += 1
        
        if guess < number_to_guess:
            result_label.config(text="Too low! Try again.")
        elif guess > number_to_guess:
            result_label.config(text="Too high! Try again.")
        else:
            result_label.config(text=f"Congratulations! You guessed it in {attempts} attempts.")
            reset_game()
            
    except ValueError:
        messagebox.showwarning("Invalid input", "Please enter a valid integer.")

# Function to reset the game
def reset_game():
    global number_to_guess, attempts
    number_to_guess = random.randint(1, 100)
    attempts = 0
    entry.delete(0, tk.END)
    result_label.config(text="Game reset! Guess the new number.")

# Setting up the GUI layout
title_label = tk.Label(root, text="Guess the Number Game", font=("Arial", 16))
title_label.pack(pady=10)

instructions_label = tk.Label(root, text="Enter a number between 1 and 100:")
instructions_label.pack()

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)

guess_button = tk.Button(root, text="Guess", command=check_guess, font=("Arial", 14))
guess_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset", command=reset_game, font=("Arial", 14))
reset_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()
