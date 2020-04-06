import os
import requests


def load_input():
    return [146810, 612564]


def is_valid(i):
    prev_c = None
    for c in str(i):
        if prev_c == c:
            break
        prev_c = c
    else:
        # print(f'No double found {i}')
        return False

    temp = i
    prev_n = 10
    while temp > 0:
        n = temp % 10
        if n > prev_n:
            # print(f'Not increasing {i}')
            return False
        prev_n = n
        temp = int(temp / 10)

    return True


def is_valid_pt2(i):
    prev_c = None
    counter = 0
    # print('>>>> ', i)
    for c in str(i):
        if prev_c == c:
            counter += 1
        elif counter > 0:
            if counter == 1:
                return True
            counter = 0
        # print(c, prev_c, counter)
        prev_c = c

    if counter == 1:
        return True

    return False


def find_passwords(min, max):
    found = []
    for i in range(min, max + 1):
        if is_valid(i) and is_valid_pt2(i):
            found.append(i)
    return found


def test_pt1():
    assert is_valid(111111) == True
    assert is_valid(223450) == False
    assert is_valid(123789) == False


def test_pt2():
    assert is_valid_pt2(112233) == True
    assert is_valid_pt2(123444) == False
    assert is_valid_pt2(111122) == True

    assert is_valid_pt2(599999) == False
    assert is_valid_pt2(559999) == True
    assert is_valid_pt2(111335) == True

test_pt1()
test_pt2()

if __name__ == '__main__':
    data = load_input()
    found = find_passwords(data[0], data[1])
    print(f'Num found: {len(found)}')
    # print('\n'.join(str(i) for i in found))
