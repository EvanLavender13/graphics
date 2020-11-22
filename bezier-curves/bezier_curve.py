import numpy as np


def linear_interpolation(p0, p1, dt):
    return (1 - dt) * p0 + dt * p1


def linear(points, dt):
    p0 = points[0]
    p1 = points[1]

    return linear_interpolation(p0, p1, dt)


def quadratic(points, dt):
    p0 = linear(points[0:2], dt)
    p1 = linear(points[1:3], dt)

    return linear_interpolation(p0, p1, dt)


def get_curve(n_segments, points):
    n_points = points.shape[0]
    dimension = points.shape[1]

    if n_points == 2:
        interp_func = linear
    elif n_points == 3:
        interp_func = quadratic
    else:
        # TODO
        interp_func = None

    t_space = np.linspace(0, 1, n_segments + 1)
    curve = np.zeros((n_segments + 1, dimension), dtype=float)

    for i, dt in enumerate(t_space):
        curve[i] = interp_func(points, dt)

    return curve
