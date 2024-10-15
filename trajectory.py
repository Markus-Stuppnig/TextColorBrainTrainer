import tkinter as tk
import time

class CircleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Circle Trajectory Game")

        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="white")
        self.canvas.pack()

        # Define lines
        self.line1_x = 200
        self.line2_x = 400
        self.canvas.create_line(self.line1_x, 0, self.line1_x, 400, fill="red", width=3)
        self.canvas.create_line(self.line2_x, 0, self.line2_x, 400, fill="blue", width=3)

        self.circle_radius = 20
        self.circle = self.canvas.create_oval(0, 180, 40, 220, fill="green")

        self.circle_visible = True
        self.moving = False
        self.start_time = None

        # Bind spacebar to checking the guess
        self.root.bind("<space>", self.check_guess)

        # Add a start button
        self.start_button = tk.Button(self.root, text="Start", command=self.start_game)
        self.start_button.pack()

    def move_circle(self):
        if self.moving:
            self.canvas.move(self.circle, 5, 0)
            pos = self.canvas.coords(self.circle)
            x1, y1, x2, y2 = pos

            if x1 >= self.line1_x and self.circle_visible:
                # self.canvas.itemconfig(self.circle, state="hidden")
                self.circle_visible = False
                ...

            if x1 < 600:
                self.root.after(50, self.move_circle)
            else:
                self.end_game()

    def start_game(self):
        self.moving = True
        self.circle_visible = True
        self.canvas.itemconfig(self.circle, state="normal")
        self.canvas.coords(self.circle, 0, 180, 40, 220)
        self.start_button.config(state=tk.DISABLED)
        self.start_time = time.time()
        self.move_circle()

    def check_guess(self, event):
        if not self.moving or self.start_time is None:
            return
        elapsed_time = time.time() - self.start_time
        projected_x = 5 * elapsed_time * 20  # Assuming speed of 5 px/step
        actual_x = self.line2_x

        if abs(projected_x - actual_x) < 20:  # Acceptable margin of error
            self.show_message("You hit the target!")
        else:
            self.show_message("You missed! Try again.")
        self.end_game()

    def show_message(self, message):
        self.canvas.create_text(300, 50, text=message, font=("Arial", 20), fill="black")

    def end_game(self):
        self.moving = False
        self.start_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    game = CircleGame(root)
    root.mainloop()
