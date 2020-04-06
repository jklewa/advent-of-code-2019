import os
import requests


session = requests.Session()
session.cookies.set(
    name='session',
    value=os.environ['ADVENTOFCODE_SESSION_TOKEN'])


def calc_fuel(mass):
    fuel = int(mass / 3) - 2
    return fuel if fuel > 0 else 0


def calc_fuel_including_fuel(mass):
    fuel = calc_fuel(mass)
    if fuel == 0:
        return 0
    return fuel + calc_fuel_including_fuel(fuel)


def load_input():
    r = session.get('https://adventofcode.com/2019/day/1/input')
    r.raise_for_status()
    return r.text.split('\n')


def test_calc_fuel():
    # For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
    assert calc_fuel(12) == 2
    # For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
    assert calc_fuel(14) == 2
    # For a mass of 1969, the fuel required is 654.
    assert calc_fuel(1969) == 654
    # For a mass of 100756, the fuel required is 33583.
    assert calc_fuel(100756) == 33583


def test_calc_fuel_including_fuel():
    # A module of mass 14 requires 2 fuel. This fuel requires no further fuel
    # (2 divided by 3 and rounded down is 0, which would call for a negative
    # fuel), so the total fuel required is still just 2.
    assert calc_fuel(14) == 2
    # At first, a module of mass 1969 requires 654 fuel. Then, this fuel
    # requires 216 more fuel (654 / 3 - 2). 216 then requires 70 more fuel,
    # which requires 21 fuel, which requires 5 fuel, which requires no further
    # fuel. So, the total fuel required for a module of mass 1969 is 654 + 216
    # + 70 + 21 + 5 = 966.
    assert calc_fuel(1969) == 654
    assert calc_fuel(654) == 216
    assert calc_fuel(216) == 70
    assert calc_fuel(70) == 21
    assert calc_fuel(21) == 5
    assert calc_fuel(5) == 0

    assert calc_fuel_including_fuel(1969) == 966
    # The fuel required by a module of mass 100756 and its fuel is: 33583 +
    # 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.

test_calc_fuel()
test_calc_fuel_including_fuel()

if __name__ == '__main__':
    total = 0
    for item in load_input():
        if not item:
            continue
        mass = int(item)
        # fuel = calc_fuel(mass)
        # print(f'Mass: {mass} -> Fuel: {fuel}')
        fuel = calc_fuel_including_fuel(mass)
        total += fuel

    print(f'Total {fuel}')
