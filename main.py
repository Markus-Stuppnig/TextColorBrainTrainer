import tkinter as tk
import random

x = 1000
y = 800

# List of colors and corresponding keys
colors = {'green': '2', 'blue': 'z', 'red': '0', 'yellow': '.'}

text_word = None

# Function to generate random colors and text
def change_colors():
    global text_word

    # Random background and text colors
    bg_color = random.choice(list(colors.keys()))
    text_word = random.choice(list(colors.keys()))

    # Ensure the text color is different from the background color
    text_color = random.choice(list(colors.keys()))
    while text_color == bg_color:
        text_color = random.choice(list(colors.keys()))

    # Clear canvas
    canvas.delete("all")

    # Generate random position for text
    x_pos = random.randint(50, x - 50)
    y_pos = random.randint(50, y - 50)

    # Draw a circle around the word (with random color)
    canvas.create_oval(x_pos - 60, y_pos - 60, x_pos + 60, y_pos + 60, fill=bg_color, outline='')

    # Place the text in the circle
    canvas.create_text(x_pos, y_pos, text=text_word, fill=text_color, font=("Helvetica", 24))

# Function to handle keypress events
def on_key(event):
    if event.char == colors[text_word]:
        print("Correct!")
        change_colors()
    else:
        print("Wrong!")
        change_colors()

# Initialize tkinter window
root = tk.Tk()
root.geometry(f"{x}x{y}")

# Canvas to draw on
canvas = tk.Canvas(root, width=x, height=y)
canvas.pack()

# Bind keys to the root window
root.bind('<Key>', on_key)

# Initial call to change the colors and position
change_colors()

# Run the tkinter main loop
root.mainloop()
