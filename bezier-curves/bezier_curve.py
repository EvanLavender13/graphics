import numpy as np


def _get_interp_func(n_points):
    if n_points == 2:
        return linear
    elif n_points == 3:
        return quadratic
    elif n_points == 4:
        return cubic
    else:
        # TODO
        return None


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


def cubic(points, dt):
    p0 = quadratic(points[0:3], dt)
    p1 = quadratic(points[1:4], dt)

    return linear_interpolation(p0, p1, dt)


def get_curve(n_segments, points):
    n_points = points.shape[0]
    dimension = points.shape[1]

    interp_func = _get_interp_func(n_points)

    t_space = np.linspace(0, 1, n_segments + 1)
    curve = np.zeros((n_segments + 1, dimension), dtype=float)

    for i, dt in enumerate(t_space):
        curve[i] = interp_func(points, dt)

    return curve