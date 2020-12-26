import numpy as np


def create_screen(screen_size):
    return np.zeros((screen_size[1], screen_size[0]), dtype=np.uint8)


def clear_screen(screen):
    return np.zeros_like(screen)


def bresenham(screen, x1, y1, x2, y2):
    # https://inst.eecs.berkeley.edu/~cs150/fa10/Lab/CP3/LineDrawing.pdf
    # TODO: make this return array of points instead of drawing itself.. maybe

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


def draw_points_p(screen, points, value=255):
    for p in points:
        draw_point_p(screen, p, value=value)


def draw_point_p(screen, p, value=255):
    draw_point_xy(screen, p[0], p[1], value=value)


def draw_points_xy(screen, points, lines=False, value=255):
    size = len(points)
    for i, (x, y) in enumerate(points):
        draw_point_xy(screen, x, y, value=value)
        if lines and i < size - 1:
            x2, y2 = points[i + 1]
            draw_line(screen, (x, y), (x2, y2))


def draw_point_xy(screen, x, y, value=255):
    row = screen.shape[0] - 1 - y
    col = x

    screen[row, col] = value


if __name__ == "__main__":
    screen = create_screen((250, 250))

    p0 = (0, 0)
    p1 = (249, 249)

    draw_line(screen, p0, p1)
    draw_point_p(screen, p0)
    draw_point_p(screen, p1)
