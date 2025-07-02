import tkinter as tk
import math
import random

root = tk.Tk()
root.title("Fresh Stack Burger - Liwag Jade")
canvas = tk.Canvas(root, width=600, height=400, bg="#fffef6")
canvas.pack()

paused = False
x_pos, y_pos = 50, 100
dx, dy = 3, 2
angle = 0

# Constants
BURGER_WIDTH = 100
BURGER_HEIGHT = 90

def random_color():
    return "#{:06x}".format(random.randint(0x444444, 0xFFFFFF))

def draw_burger_with_centered_name(x, y, name="Liwag Jade"):
    parts = {}

    # Top bun (light golden)
    parts['top_bun'] = canvas.create_oval(x, y, x + BURGER_WIDTH, y + 30, fill="#ffdb99", outline="#e6ac5d", width=2)

    # Lettuce
    parts['lettuce'] = canvas.create_arc(x + 10, y + 26, x + 90, y + 45, start=0, extent=180, fill="#b8f5b1", outline="#63b26e")

    # Tomato
    parts['tomato'] = canvas.create_oval(x + 20, y + 42, x + 80, y + 50, fill="#ff7b7b", outline="#c94f4f")

    # Patty
    parts['patty'] = canvas.create_rectangle(x + 25, y + 50, x + 75, y + 60, fill="#b5651d", outline="#5c3317")

    # Cheese
    parts['cheese'] = canvas.create_polygon(x + 20, y + 60, x + 80, y + 60, x + 70, y + 72, x + 30, y + 72,
                                            fill="#fff8a4", outline="#d1c266")

    # Bottom bun
    parts['bottom_bun'] = canvas.create_oval(x, y + 70, x + BURGER_WIDTH, y + BURGER_HEIGHT,
                                             fill="#ffdb99", outline="#e6ac5d", width=2)

    # Centered name
    parts['name_text'] = canvas.create_text(
        x + BURGER_WIDTH / 2,
        y + BURGER_HEIGHT / 2,
        text=name,
        font=("Arial", 11, "bold"),
        fill="#4b2e00"
    )

    return parts

burger_parts = draw_burger_with_centered_name(x_pos, y_pos)

def change_burger_colors():
    canvas.itemconfig(burger_parts['top_bun'], fill=random_color())
    canvas.itemconfig(burger_parts['lettuce'], fill=random_color())
    canvas.itemconfig(burger_parts['tomato'], fill=random_color())
    canvas.itemconfig(burger_parts['patty'], fill=random_color())
    canvas.itemconfig(burger_parts['cheese'], fill=random_color())
    canvas.itemconfig(burger_parts['bottom_bun'], fill=random_color())

def move_burger():
    global x_pos, y_pos, dx, dy, angle

    if not paused:
        x_pos += dx
        y_pos += dy
        angle += 0.05
        wave_y = math.sin(angle) * 5

        coords = canvas.coords(burger_parts['top_bun'])
        curr_x, curr_y = coords[0], coords[1]
        delta_x = x_pos - curr_x
        delta_y = (y_pos + wave_y) - curr_y

        for part in burger_parts.values():
            canvas.move(part, delta_x, delta_y)

        # Bounce on walls
        if x_pos <= 0 or x_pos >= 600 - BURGER_WIDTH:
            dx *= -1
            change_burger_colors()  # <-- Color changes on side bounce only

        if y_pos <= 0 or y_pos >= 400 - BURGER_HEIGHT:
            dy *= -1

    canvas.after(30, move_burger)

def toggle_pause(event):
    global paused
    paused = not paused

root.bind("<Key>", toggle_pause)
move_burger()
root.mainloop()