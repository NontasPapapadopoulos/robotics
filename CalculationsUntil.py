import math


def arm_calculations(x2, y2, L1, L2):
    epsilon = 0.0001

    ya2 = float(0)

    C = (y2 ** 2 + x2 ** 2 + L1 ** 2 - L2 ** 2) / 2
    D = 4 * C ** 2 * y2 ** 2 - 4 * (x2 ** 2 + y2 ** 2) * (C ** 2 - L1 ** 2 * x2 ** 2)

    if abs(x2) < epsilon:
        ya1 = C / y2
        ya2 = ya2
        xa1 = math.sqrt(L1 ** 2 - (C ** 2 / y2 ** 2))
        xa2 = - xa1
    else:
        ya1 = (2 * C * y2 + math.sqrt(D)) / (2 * (x2 ** 2 + y2 ** 2))
        ya2 = (2 * C * y2 - math.sqrt(D)) / (2 * (x2 ** 2 + y2 ** 2))
        xa1 = (C - y2 * ya1) / x2
        xa2 = (C - y2 * ya2) / x2

    return xa1, ya1, xa2, ya2


def calculate_x1_and_y1(x2, y2, L1, L2, LR):
    coordinates = arm_calculations(x2, y2, L1, L2)

    f11 = math.atan2(coordinates[0], coordinates[1])
    x2_11 = x2 * math.cos(f11) - y2 * math.sin(f11)
    y2_11 = x2 * math.sin(f11) + y2 * math.cos(f11)

    f12 = abs(math.atan2(x2_11, y2_11) * (180 / math.pi))

    if 0 < f12 < 180 and not LR and x2 > 0:
        x1 = coordinates[2]
        y1 = coordinates[3]
    elif 0 < f12 < 180 and not LR and x2 <= 0:
        x1 = coordinates[0]
        y1 = coordinates[1]
    elif x2 > 0 and LR:
        x1 = coordinates[0]
        y1 = coordinates[1]
    else:
        x1 = coordinates[2]
        y1 = coordinates[3]

    return x1, y1


def is_workspace_is_valid(x, y, L1, L2):
    # check if a point is inside or outside of workspace
    is_p1_inside_of_the_outer_circle = x ** 2 + y ** 2 < (L1 + L2) ** 2
    is_p1_out_of_the_inner_circle = x ** 2 + y ** 2 > (L1 - L2) ** 2

    if is_p1_out_of_the_inner_circle and is_p1_inside_of_the_outer_circle:
        return True

    print('Coordinates ', x, y, ' are outside of workspace!')
    return False


def arm_movement_is_valid(L1, L2, x2, y2, xt, yt):
    a = (y2 - yt) / (x2 - xt)
    b = y2 ** 2 - a * x2 ** 2
    D = 4 * a ** 2 * b ** 2 * -4 * (a ** 2 + 1) * (b ** 2 - (L1 - L2) ** 2)
    return D < 0 or D == 0







