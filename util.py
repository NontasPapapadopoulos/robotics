import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from graphics import *

from CalculationsUntil import calculate_x1_and_y1

background_color = "white"


def create_window(screen_width, screen_height):
    win = GraphWin("Robot Arm Simulation", screen_width, screen_height)
    win.setCoords(
        (screen_width / 2) * -1,
        (screen_height / 2) * -1,
        screen_width / 2,
        screen_width / 2
    )
    win.setBackground(background_color)
    design_axes(win, screen_width, screen_height, "green")

    return win


def draw_line(x1, y1, x2, y2, window, width, color):
    line = Line(Point(x1, y1), Point(x2, y2))
    line.setWidth(width)
    line.setFill(color)
    line.draw(window)


def draw_circle(x1, y1, radius, window, width, color, fillcolor=''):
    circle = Circle(Point(x1, y1), radius)
    circle.setWidth(width)
    circle.setOutline(color)
    if fillcolor != '':
        circle.setFill(fillcolor)
    circle.draw(window)


def design_axes(window, screen_width, screen_height, color):
    draw_line((screen_width / 2) * -1, 0, screen_width / 2, 0, window, 2, color)  # X
    draw_line(0, (screen_height / 2) * -1, 0, screen_height / 2, window, 2, color)  # Y


def input_value_from_pop_up_window(message):
    while True:
        try:
            root = tk.Tk()
            root.withdraw()
            user_input = simpledialog.askstring("Είσοδος δεδομένων: ", message)
            a = float(user_input)
            break
        except ValueError as e:
            print(f"Error: {e}")
            tk.messagebox.showerror("Σφάλμα", f"Μη έγκυρη είσοδος: {e}")
    return a


def selectArmDirection():
    while True:
        try:
            result = messagebox.askquestion("Arm direction", "Do you want right direction? ", )
            if result:
                LR = 0
            else:
                LR = 1
        except WindowsError as win_err:
            print("An error occurred:\n{}".format(win_err))

        if LR == 0 or LR == 1 == True:
            break


def showErrorMessage(message):
    messagebox.showerror("Error", message)


def draw_horizontal_vertical_axes(win, x1, x2, y1, y2):
    draw_line(0, 0, x1, y1, win, 3, "black")
    draw_line(x1, y1, x2, y2, win, 3, "black")


def draw_inner_and_outer_circles(L1, L2, win):
    draw_circle(0, 0, L1 + L2, win, 3, "red")
    draw_circle(0, 0, abs(L1 - L2), win, 3, "red")


def draw_the_arm(x1, y1, x2, y2, win):
    draw_line(0, 0, x1, y1, win, 3, "black")
    draw_line(x1, y1, x2, y2, win, 3, "black")


def draw_linear_movement_line(x2, y2, xt, yt, win):
    draw_line(x2, y2, xt, yt, win, 3, "blue")




def display_arm_movement_animation(L1, L2, direction, screen_height, screen_width, win, x1, x2, xt, y1, y2, yt):
    draw_linear_movement_line(x2, y2, xt, yt, win)
    draw_circle(0, 0, abs(L1 + L2), win, 2, "blue", "yellow")
    design_axes(win, screen_width, screen_height, "green")
    # Animation
    animation_duration = 5
    rate = 10
    points = int(animation_duration * rate)
    delay = 1 / rate
    for i in range(0, points + 1):
        xp = float((xt - x2) * i / points + x2)
        yp = float((yt - y2) * i / points + y2)

        draw_circle(0, 0, L1 + L2, win, 2, "blue")
        draw_circle(0, 0, abs(L1 - L2), win, 2, "blue", "yellow")
        design_axes(win, screen_width, screen_height, "green")

        draw_linear_movement_line(x2, y2, xt, yt, win)

        x1m, y1m = calculate_x1_and_y1(xp, yp, L1, L2, direction)

        draw_line(0, 0, x1, y1, win, 3, background_color)
        draw_line(x1, y1, x2, y2, win, 3, background_color)
        draw_circle(x1, y1, 3, win, 2, background_color)
        draw_circle(x2, y2, 3, win, 2, background_color)

        draw_line(0, 0, x1m, y1m, win, 3, "black")
        draw_line(x1m, y1m, xp, yp, win, 2, "black")
        draw_circle(x1m, y1m, 3, win, 2, "red")
        draw_circle(xp, yp, 3, win, 2, "red")
        time.sleep(delay)

        draw_line(0, 0, x1m, y1m, win, 3, background_color)
        draw_line(x1m, y1m, xp, yp, win, 3, background_color)
        draw_circle(x1m, y1m, 3, win, 2, background_color)
        draw_circle(xp, yp, 3, win, 2, background_color)