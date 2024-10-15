import tkinter as tk
import random
import time

x = 1000
y = 800

# List of colors and corresponding keys
colors = {'green': '2', 'blue': 'z', 'red': '0', 'yellow': '.'}

text_word = None
last_time = None
times = []

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
    x_pos = 65 if random.randint(0, 1) == 0 else x - 65
    y_pos = 65 if random.randint(0, 1) == 0 else y - 65

    # Draw a circle around the word (with random color)
    canvas.create_oval(x_pos - 60, y_pos - 60, x_pos + 60, y_pos + 60, fill='', outline=bg_color, width=5)

    # Place the text in the circle
    canvas.create_text(x_pos, y_pos, text=text_word, fill=text_color, font=("Helvetica", 24))

# Function to handle keypress events
def on_key(event):
    global last_time
    if event.char == colors[text_word]:
        print("Correct!")
        change_colors()
    else:
        print("Wrong!")
        change_colors()

    if last_time is not None:
        times.append(time.time() - last_time)
        print(times[-1])
    last_time = time.time()

# Initialize tkinter window
root = tk.Tk()
root.geometry(f"{x}x{y}")
root.config(bg="black")

# Canvas to draw on
canvas = tk.Canvas(root, width=x, height=y, bg="black", highlightthickness=0)
canvas.pack()

# Bind keys to the root window
root.bind('<Key>', on_key)

# Initial call to change the colors and position
change_colors()

# Run the tkinter main loop
root.mainloop()
