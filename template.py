import os
import requests


session = requests.Session()
session.cookies.set(
    name='session',
    value=os.environ['ADVENTOFCODE_SESSION_TOKEN'])


def load_input():
    r = session.get('https://adventofcode.com/2019/day/3/input')
    r.raise_for_status()
    return [int(i) for i in r.text.split(',')]


def test():
    assert False

test()

if __name__ == '__main__':
    data = load_input()

    pt1 = data.copy()
