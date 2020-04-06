import os
import requests
from copy import deepcopy


session = requests.Session()
session.cookies.set(
    name='session',
    value=os.environ['ADVENTOFCODE_SESSION_TOKEN'])


def load_input():
    r = session.get('https://adventofcode.com/2019/day/3/input')
    r.raise_for_status()
    return [i.strip() for i in r.text.split('\n')]


def path(s):
    x = 0
    y = 0
    p = list()
    for move in s.split(','):
        direction, amount = move[0], int(move[1:])
        y_d, x_d = 0, 0

        if direction == 'U':
            y_d = 1
        if direction == 'D':
            y_d = -1
        if direction == 'L':
            x_d = -1
        if direction == 'R':
            x_d = 1

        for i in range(0, amount):
            x += x_d
            y += y_d
            p.append((x, y))

    return p


def intersect(path_a, path_b):
    b_points = set(path_b)
    return [
        point for point in path_a if point in b_points
    ]


def manhattan_distance(point):
    return abs(point[0]) + abs(point[1])


def path_distance(point, path):
    return path.index(point) + 1


def intersect_distance(a, b):
    return min(
        manhattan_distance(point)
        for point in intersect(
            path(a),
            path(b)
        )
    )


def signal_delay(a, b):
    path_a = path(a)
    path_b = path(b)
    return min(
        path_distance(point, path_a) + path_distance(point, path_b)
        for point in intersect(
            path_a,
            path_b
        )
    )


def test():
    a = 'R8,U5,L5,D3'
    b = 'U7,R6,D4,L4'
    assert intersect_distance(a, b) == 6

    a = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
    b = 'U62,R66,U55,R34,D71,R55,D58,R83'
    assert intersect_distance(a, b) == 159

    a = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
    b = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
    assert intersect_distance(a, b) == 135


def test_pt2():
    a = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
    b = 'U62,R66,U55,R34,D71,R55,D58,R83'
    assert signal_delay(a, b) == 610

    a = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
    b = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
    assert signal_delay(a, b) == 410

test()
test_pt2()

if __name__ == '__main__':
    data = load_input()

    pt1 = deepcopy(data)
    d = intersect_distance(pt1[0], pt1[1])
    print(f'Intersect distance: {d}')

    pt2 = deepcopy(data)
    d = signal_delay(pt2[0], pt2[1])
    print(f'Signal delay: {d}')
