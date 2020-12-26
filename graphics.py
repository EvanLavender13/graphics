import numpy as np


def create_screen(screen_size):
    return np.zeros((screen_size[1], screen_size[0]), dtype=np.uint8)


def clear_screen(screen):
    return np.zeros_like(screen)


def bresenham(screen, x0, y0, x1, y1):
    # https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm
    # TODO: make this return array of points instead of drawing itself... maybe?

    dx = np.abs(x1 - x0)
    sx = 1 if x0 < x1 else -1
    dy = -np.abs(y1 - y0)
    sy = 1 if y0 < y1 else -1
    err = dx + dy

    x = x0
    y = y0

    while True:
        draw_point(screen, x, y)

        if x == x1 and y == y1:
            break

        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x += sx

        if e2 <= dx:
            err += dx
            y += sy


def draw_line(screen, p0, p1):
    x0, y0 = p0
    x1, y1 = p1

    bresenham(screen, x0, y0, x1, y1)


def draw_points(screen, points, lines=False, connect=False, value=255):
    size = len(points)

    for i, (x, y) in enumerate(points):
        draw_point(screen, x, y, value=value)

        if lines and i < size - 1:
            x1, y1 = points[i + 1]
            draw_line(screen, (x, y), (x1, y1))

    if connect and lines:
        x0, y0 = points[-1, 0], points[-1, 1]
        x1, y1 = points[0, 0], points[0, 1]
        draw_line(screen, (x0, y0), (x1, y1))


def draw_point(screen, x, y, value=255):
    row = screen.shape[0] - 1 - y
    col = x

    screen[row, col] = value


if __name__ == "__main__":
    screen = create_screen((250, 250))
