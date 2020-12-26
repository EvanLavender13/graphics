import numpy as np


def create_screen(screen_size):
    return np.zeros((screen_size[1], screen_size[0]), dtype=np.uint8)


def clear_screen(screen):
    return np.zeros_like(screen)


def bresenham(screen, x0, y1, x1, y2):
    # https://inst.eecs.berkeley.edu/~cs150/fa10/Lab/CP3/LineDrawing.pdf
    # TODO: make this return array of points instead of drawing itself.. maybe

    steep = np.abs(y2 - y1) > np.abs(x1 - x0)
    if steep:
        x0, y1 = y1, x0
        x1, y2 = y2, x1

    if x0 > x1:
        x0, x1 = x1, x0
        y1, y2 = y2, y1

    d_err = np.abs(y2 - y1)
    y_step = -1 if y1 > y2 else 1
    dx = x1 - x0

    err = dx >> 1
    y = y1

    for x in range(x0, x1):
        if steep:
            draw_point(screen, y, x)
        else:
            draw_point(screen, x, y)

        err -= d_err
        if err < 0:
            y += y_step
            err += dx


def draw_line(screen, p0, p1):
    x0, y1 = p0
    x1, y2 = p1

    bresenham(screen, x0, y1, x1, y2)


def draw_points(screen, points, lines=False, connect=False, value=255):
    size = len(points)

    for i, (x, y) in enumerate(points):
        draw_point(screen, x, y, value=value)

        if lines and i < size - 1:
            x1, y2 = points[i + 1]
            draw_line(screen, (x, y), (x1, y2))

    if connect and lines:
        x0, y1 = points[-1, 0], points[-1, 1]
        x1, y2 = points[0, 0], points[0, 1]
        draw_line(screen, (x0, y1), (x1, y2))


def draw_point(screen, x, y, value=255):
    row = screen.shape[0] - 1 - y
    col = x

    screen[row, col] = value


if __name__ == "__main__":
    screen = create_screen((250, 250))
