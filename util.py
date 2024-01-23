import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from graphics import *


def createWindow(screen_width, screen_height):
    background_color = "white"

    win = GraphWin("Robot Arm Simulation", screen_width, screen_height)
    win.setCoords(
        (screen_width / 2) * -1,
        (screen_height / 2) * -1,
        screen_width / 2,
        screen_width / 2
    )
    win.setBackground(background_color)
    DesignAxes(win, screen_width, screen_height, "green")

    return win


def DrawLine(x1, y1, x2, y2, window, width, color):
    line = Line(Point(x1, y1), Point(x2, y2))
    line.setWidth(width)
    line.setFill(color)
    line.draw(window)


def DrawCircle(x1, y1, radius, window, width, color, fillcolor=''):
    aCircle = Circle(Point(x1, y1), radius)
    aCircle.setWidth(width)
    aCircle.setOutline(color)
    if fillcolor != '':
        aCircle.setFill(fillcolor)
    aCircle.draw(window)


def DesignAxes(window, screen_width, screen_height, color):
    DrawLine((screen_width / 2) * -1, 0, screen_width / 2, 0, window, 2, color)  # X
    DrawLine(0, (screen_height / 2) * -1, 0, screen_height / 2, window, 2, color)  # Y


def inputValueFromPopUpWindow(message):
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
            if result == True:
                LR = 0
            else:
                LR = 1
        except WindowsError as win_err:
            print("An error occurred:\n{}".format(win_err))

        if LR == 0 or LR == 1 == True:
            break
