from win32api import GetSystemMetrics
from util import *
from CalculationsUntil import *


def program():
    screen_width = GetSystemMetrics(0) * 0.25
    screen_height = GetSystemMetrics(1) * 0.75

    win = create_window(screen_width, screen_height)

    try:
        L1 = input_value_from_pop_up_window('Δώσε το μήκος L1 του πρώτου μέλους του ρομποτικού βραχίονα')
        L2 = input_value_from_pop_up_window('Δώσε το μήκος L2 του δεύτερου μέλους του ρομποτικού βραχίονα')
        if L1 + L2 > screen_height:
            print(
                'Tα μεγέθη των βραχιόνων θα πρεπει να ειναι μικρότερα απο τις διαστάσεις της οθόνης: ' + screen_width / 2 + ' ή ' + screen_height / 2)

        draw_inner_and_outer_circles(L1, L2, win)

        direction = selectArmDirection()

        x2 = input_value_from_pop_up_window("Δώσε τη συντεταγμένη Χ2 του άκρου του 2ου μέλους: ")
        y2 = input_value_from_pop_up_window("Δώσε τη συντεταγμένη Y2 του άκρου του 2ου μέλους: ")

        x1, y1 = calculate_x1_and_y1(x2, y2, L1, L2, direction)

        draw_the_arms(x1, y1, x2, y2, win)

        while True:
            xt = input_value_from_pop_up_window("Δώσε τη θέση Χ που θέλεις να πάει το ρομπότ: ")
            yt = input_value_from_pop_up_window("Δώσε τη θέση Υ που θέλεις να πάει το ρομπότ: ")

            if is_workspace_is_valid(x2, y2, L1, L1) and arm_movement_is_valid(L1, L2, x2, y2, xt, yt, direction, points):
                display_arm_movement_animation(L1, L2, direction, screen_height, screen_width, win, x1, x2, xt, y1, y2, yt)
                break
            else:
                show_error_dialog("Η κίνηση δεν ειναι εφυκτή")


    except WindowsError:
        print('An error occurred: ' + WindowsError)

    win.getMouse()


if __name__ == '__main__':
    program()
