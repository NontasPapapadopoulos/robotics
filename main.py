from win32api import GetSystemMetrics
from util import *
from CalculationsUntil import *


def program():
    screen_width = GetSystemMetrics(0) * 0.25
    screen_height = GetSystemMetrics(1) * 0.75

    win = createWindow(screen_width, screen_height)

    try:
        L1 = inputValueFromPopUpWindow('Δώσε το μήκος L1 του πρώτου μέλους του ρομποτικού βραχίονα')
        L2 = inputValueFromPopUpWindow('Δώσε το μήκος L2 του δεύτερου μέλους του ρομποτικού βραχίονα')
        if L1 + L2 > screen_height:
            print('Tα μεγέθη των βραχιόνων θα πρεπει να ειναι μικρότερα απο τις διαστάσεις της οθόνης: ' + screen_width / 2 + ' ή ' + screen_height / 2)

        direction = selectArmDirection()

        x2 = inputValueFromPopUpWindow("Δώσε τη συντεταγμένη Χ2 του άκρου του 2ου μέλους: ")
        y2 = inputValueFromPopUpWindow("Δώσε τη συντεταγμένη Y2 του άκρου του 2ου μέλους: ")

        xt = inputValueFromPopUpWindow("Δώσε τη θέση Χ που θέλεις να πάει το ρομπότ: ")
        yt = inputValueFromPopUpWindow("Δώσε τη θέση Υ που θέλεις να πάει το ρομπότ: ")

        x1, y1 = calculateX1andY1(x2, y2, L1, L2, direction)

        if isWorkSpaceValid(x2, y2, L1, L1) and armMovementIsValid(L1, L2, x2, y2, xt, yt):
            DrawLine(x2, y2, xt, yt, win, 3, "blue")  # Σχεδιασμός της ευθείας της κίνησης
            DrawLine(x2, y2, xt, yt, win, 3, "white")
            DrawCircle(0, L1 + L2, win, 2, "blue")
            DrawCircle(0, 0, abs(L1 + L2), win, 2, "blue", "yellow")
            DesignAxes(win, screen_width, screen_height, "green")
            DrawLine(0, 0, x1, y1, win, 3, "black")
            DrawLine(x1, y1, x2, y2, win, 3, "black")

        x1, y1 = calculateX1andY1(x2, y2, L1, L2, direction)

        # Παράμετροι Animation
        animation_duration = 15  # διάρκεια της κίνησης σε δευτερόλεπτα
        Rate = 20  # καρέ ανά δευτερόλεπτο
        Points = int(animation_duration * Rate)  # συνολικά βήματα της κίνησης
        DelaySec = 1 / Rate  # Υπολογισμός της καυθστέρησης

        DrawCircle(0, 0, L1 + L2, win, 3, "red")
        DrawCircle(0, 0, abs(L1 - L2), win, 3, "red")

        DrawLine(0, 0, x1, y1, win, 3, "black")
        DrawLine(x1, y1, x2, y2, win, 3, "black")

        for i in range(0, Points + 1):
            xp = float((xt - x2) * i / Points + x2)
            yp = float((yt - y2) * i / Points + y2)

            DrawCircle(0, 0, L1 + L2, win, 2, "blue")
            DrawCircle(0, 0, abs(L1 - L2), win, 2, "blue", "yellow")
            DesignAxes(win, screen_width, screen_height, "green")  # Καρτεσιανές συντεταγμένες

            DrawLine(x2, y2, xt, yt, win, 3, "blue")  # Σχεδιασμός της ευθείας κίνησης

            X1m, Y1m = calculateX1andY1(xp, yp, L1, L2, direction)
            ColorBackground = "white"

            DrawLine(0, 0, x1, y1, win, 3, ColorBackground)  # Σβήνω την απλή γραμμή
            DrawLine(x1, y1, x2, y2, win, 3, ColorBackground)
            DrawCircle(x1, y1, 3, win, 2, ColorBackground)
            DrawCircle(x2, y2, 3, win, 2, ColorBackground)

            DrawLine(0, 0, X1m, Y1m, win, 3, "black")  # Σχεδιάζω τη γραμμή στη νέα θέση
            DrawLine(X1m, Y1m, xp, yp, win, 2, "black")
            DrawCircle(X1m, Y1m, 3, win, 2, "red")
            DrawCircle(xp, yp, 3, win, 2, "red")
            time.sleep(DelaySec)  # Χρονοκαθυστέρηση για τον χρήστη
            DrawLine(0, 0, X1m, Y1m, win, 3, ColorBackground)  # Σβήνω την απλή γραμμή
            DrawLine(X1m, Y1m, xp, yp, win, 3, ColorBackground)
            DrawCircle(X1m, Y1m, 3, win, 2, ColorBackground)
            DrawCircle(xp, yp, 3, win, 2, ColorBackground)

        # Τελική απεικόνιση του βραχίονα

        DrawCircle(0, 0, L1 + L2, win, 2, "blue")
        DrawCircle(0, 0, abs(L1 + L2), win, 2, "blue", "yellow")
        DesignAxes(win, screen_width, screen_height, "green")  # Καρτεσιανές συντεταγμένες
        DrawLine(0, 0, X1m, Y1m, win, 3, "black")
        DrawLine(X1m, Y1m, xp, yp, win, 3, "black")
        DrawCircle(X1m, Y1m, 3, win, 2, "red")
        DrawCircle(xp, yp, 3, win, 2, "red")
        DrawLine(x2, y2, xt, yt, win, 3, "blue")  # Σχεδιασμός της ευθείας κίνησης



    except WindowsError:
        print('An error occurred: ' + WindowsError)



    win.getMouse()


if __name__ == '__main__':
    program()

# find workspace and check atn2??
