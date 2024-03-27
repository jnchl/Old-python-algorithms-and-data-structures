import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)


def orientation(p, q, r):
    direction = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)

    if direction == 0:
        return 0
    elif direction > 0:
        return 1
    else:
        return 2


def in_between(p, q, r):
    return q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x) and q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y)


def jarvis(point_array, use_colinear_check):
    points_amount = len(point_array)

    if points_amount < 3:
        raise ValueError

    leftest_point = Point(np.inf, 0)
    leftest_point_index = None

    for point_index in range(points_amount):
        if point_array[point_index].x < leftest_point.x:
            leftest_point = point_array[point_index]
            leftest_point_index = point_index

    hull_indexes = []

    p_index = leftest_point_index
    q_index = None
    while True:

        hull_indexes.append(p_index)

        q_index = (p_index + 1) % points_amount

        for i in range(points_amount):

            p = point_array[p_index]
            q = point_array[i]
            r = point_array[q_index]

            if orientation(p, q, r) == 2:
                q_index = i

            if use_colinear_check and p_index != i and orientation(p, r, q) == 0 and in_between(p, r, q):
                q_index = i

        p_index = q_index

        if p_index == leftest_point_index:
            break

    hull_points = [point_array[index] for index in hull_indexes]
    return hull_points


points = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]
points_a = [Point(t[0], t[1]) for t in points]

print(jarvis(points_a, use_colinear_check=False))
print(jarvis(points_a, use_colinear_check=True))