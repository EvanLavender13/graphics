import numpy as np


def create_screen(screen_size):
    return np.zeros((screen_size[1], screen_size[0]), dtype=float)


def clear_screen(screen):
    return np.zeros_like(screen)


def bresenham(screen, x1, y1, x2, y2):
    # https://inst.eecs.berkeley.edu/~cs150/fa10/Lab/CP3/LineDrawing.pdf
    # TODO: make this return array of points instead of drawing itself

    steep = np.abs(y2 - y1) > np.abs(x2 - x1)
    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    d_err = np.abs(y2 - y1)
    y_step = -1 if y1 > y2 else 1
    dx = x2 - x1

    err = dx >> 1
    y = y1

    for x in range(x1, x2):
        if steep:
            draw_point_xy(screen, y, x)
        else:
            draw_point_xy(screen, x, y)

        err -= d_err
        if err < 0:
            y += y_step
            err += dx


def draw_line(screen, p0, p1):
    x1, y1 = p0
    x2, y2 = p1

    bresenham(screen, x1, y1, x2, y2)


def draw_points_p(screen, points, value=2):
    for p in points:
        draw_point_p(screen, p, value=value)


def draw_point_p(screen, p, value=2):
    draw_point_xy(screen, p[0], p[1], value=value)


def draw_points_xy(screen, points, value=1):
    for x, y in points:
        draw_point_xy(screen, x, y, value=value)


def draw_point_xy(screen, x, y, value=1):
    row = screen.shape[0] - 1 - y
    col = x

    screen[row, col] = value


def print_screen(screen):
    # height, width = screen.shape

    for y, row in enumerate(screen):
        # TODO
        line = "|"
        for x, _ in enumerate(row):
            value = screen[y, x]
            # TODO
            if value == 1:
                pixel = " . "
            elif value == 2:
                pixel = " O "
            else:
                pixel = "   "

            line += pixel

        print(line + "|")


if __name__ == "__main__":
    screen = create_screen((25, 25))

    p0 = (0, 0)
    p1 = (24, 24)

    draw_line(screen, p0, p1)
    draw_point_p(screen, p0)
    draw_point_p(screen, p1)

    print_screen(screen)
