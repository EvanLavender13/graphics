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
        return general


def _get_parameter_space(n_segments):
    return np.linspace(0, 1, n_segments + 1)


def _binomial_coefficients(n, i):
    return np.math.factorial(n) / np.math.factorial(i) / np.math.factorial(n - i)


def _bernstein_polynomial(dt, n, i):
    return _binomial_coefficients(n, i) * (1 - dt) ** (n - i) * dt ** i


def linear(p0, p1, dt):
    return (1 - dt) * p0 + dt * p1


def quadratic(p0, p1, p2, dt):
    return linear(
        linear(p0, p1, dt),
        linear(p1, p2, dt),
        dt
    )


def cubic(p0, p1, p2, p3, dt):
    return linear(
        quadratic(p0, p1, p2, dt),
        quadratic(p1, p2, p3, dt),
        dt
    )


def general(points, dt):
    n = points.shape[0] - 1

    point = np.zeros_like(points[0])
    for i, p in enumerate(points):
        point += _bernstein_polynomial(dt, n, i) * p

    return point


def get_curve(n_segments, points):
    n_points = points.shape[0]
    dimension = points.shape[1]

    interp_func = _get_interp_func(n_points)
    t_space = _get_parameter_space(n_segments)

    curve = np.zeros((n_segments + 1, dimension), dtype=float)
    for i, dt in enumerate(t_space):
        curve[i] = interp_func(*points, dt)

    return curve
