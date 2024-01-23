from win32api import GetSystemMetrics
from util import *
from CalculationsUntil import *

def program():
    screen_width = GetSystemMetrics(0) * 0.25
    screen_height = GetSystemMetrics(1) * 0.75

    win = createWindow(screen_width, screen_height)

    while True:
        try:
            direction = selectArmDirection()
            L1 = inputValueFromPopUpWindow('Δώσε το μήκος L1 του πρώτου μέλους του ρομποτικού βραχίονα')
            L2 = inputValueFromPopUpWindow('Δώσε το μήκος L2 του δεύτερου μέλους του ρομποτικού βραχίονα')

            x2 = inputValueFromPopUpWindow("Δώσε το σημείο Χ2: ")
            y2 = inputValueFromPopUpWindow("Δώσε το σημείο Υ2: ")

            if L1 + L2 < screen_height:
                break
            else:
                print(
                    'Tα μεγέθη των βραχιόνων θα πρεπει να ειναι μικρότερα απο τις διαστάσεις της οθόνης: ' + screen_width / 2 + ' ή ' + screen_height / 2)

        except WindowsError:
            print('An error occurred: ' + WindowsError)

    x1, y1 = calculateX1andY1(x2, y2, L1, L2, direction)

    DrawCircle(0, 0, L1 + L2, win, 3, "red")
    DrawCircle(0, 0, abs(L1 - L2), win, 3, "red")

    DrawLine(0, 0, x1, y1, win, 3, "black")
    DrawLine(x1, y1, x2, y2, win, 3, "black")

    win.getMouse()


if __name__ == '__main__':
    program()
