import math


def armCalculations(x2, y2, L1, L2):
    epsilon = 0.0001

    xa1 = float(0)
    ya1 = float(0)
    xa2 = float(0)
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


def calculateX1andY1(x2, y2, L1, L2, LR):
    coordinates = armCalculations(x2, y2, L1, L2)

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


def finalArm(x2, y2, L1, L2, LR):
    xa1 = float(0)
    ya1 = float(0)
    xa2 = float(0)
    ya2 = float(0)

    xa1, ya1, xa2, ya2 = armCalculations(x2, y2, L1, L2)

    f11 = math.atan2(xa1, ya1)

    xtn = (x2 - xa1) * math.cos(-f11) - (y2 - ya1) * math.sin(-f11)
    ytn = (x2 - xa1) * math.sin(-f11) + (y2 - ya1) * math.cos(-f11)

    f22 = math.atan2(xtn, ytn)

    x1 = float(0)
    y1 = float(0)

    if LR == 0:  # left direction
        if f22 <= math.pi:
            x1 = xa1
            y1 = ya1
        else:
            x1 = xa2
            y1 = ya2
    else:
        if f22 > math.pi:
            x1 = xa1
            y1 = ya1
        else:
            x1 = xa2
            y2 = ya2

    return x1, y1
