import numpy as np


_cubic_coefs = np.array([
    [1, 0, 0, 0],
    [-3, 3, 0, 0],
    [3, -6, 3, 0],
    [-1, 3, -3, 1]
])


def _cubic_params(u):
    return np.array([1, u, u ** 2, u ** 3])


def linear(p0, p1, u):
    return (1 - u) * p0 + u * p1


def quadratic(p0, p1, p2, u):
    p0_u = linear(p0, p1, u)
    p1_u = linear(p1, p2, u)

    return linear(p0_u, p1_u, u)


def cubic(p0, p1, p2, p3, u):
    p0_u = quadratic(p0, p1, p2, u)
    p1_u = quadratic(p1, p2, p3, u)

    return linear(p0_u, p1_u, u)


def _de_casteljaus(points, u):
    if len(points) == 1:
        return points[0]
    else:
        p0 = _de_casteljaus(points[0:-1], u)
        p1 = _de_casteljaus(points[1:], u)

        return linear(p0, p1, u)


def bezier_curve(control_points, n_samples):
    u_space = np.linspace(0, 1, n_samples)
    curve = np.zeros((n_samples, 2), dtype=int)

    for i, u in enumerate(u_space):
        curve[i] = _de_casteljaus(control_points, u)

    return curve


def cubic_bezier(control_points, n_samples):
    u_space = np.linspace(0, 1, n_samples)
    curve = np.zeros((n_samples, 2), dtype=int)

    for i, u in enumerate(u_space):
        curve[i] = _cubic_params(u) @ _cubic_coefs @ control_points

    return curve
