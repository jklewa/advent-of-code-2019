import os
import requests


session = requests.Session()
session.cookies.set(
    name='session',
    value=os.environ['ADVENTOFCODE_SESSION_TOKEN'])

OPCODE_1 = 1  # add
OPCODE_2 = 2  # multiply
OPCODE_99 = 99  # halt


def load_input():
    r = session.get('https://adventofcode.com/2019/day/2/input')
    r.raise_for_status()
    return [int(i) for i in r.text.split(',')]


def opcode(op):
    if op == OPCODE_1:
        return OPCODE_1
    if op == OPCODE_2:
        return OPCODE_2
    if op == OPCODE_99:
        return OPCODE_99
    raise NotImplementedError(f'{op} is not a valid OPCODE')


def op_add(pos, data):
    input_a_pos = data[pos + 1]
    input_b_pos = data[pos + 2]
    output_pos = data[pos + 3]

    input_a = data[input_a_pos]
    input_b = data[input_b_pos]
    data[output_pos] = input_a + input_b
    return True


def op_multiply(pos, data):
    input_a_pos = data[pos + 1]
    input_b_pos = data[pos + 2]
    output_pos = data[pos + 3]

    input_a = data[input_a_pos]
    input_b = data[input_b_pos]
    data[output_pos] = input_a * input_b
    return True


def op_halt(pos, data):
    # print(f'Program Halted at idx {pos} : {data}')
    return False


def op(code):
    if code == OPCODE_1:
        return op_add
    if code == OPCODE_2:
        return op_multiply
    if code == OPCODE_99:
        return op_halt
    raise NotImplementedError(f'{code} is not a valid OPCODE')


def next_op(current_pos):
    return current_pos + 4


def program(data):
    ok = True
    pos = 0
    while ok:
        code = data[pos]
        ok = op(code)(pos, data)
        pos = next_op(pos)


def test_opcode():
    assert opcode(1) == OPCODE_1
    assert opcode(2) == OPCODE_2
    assert opcode(99) == OPCODE_99
    try:
        opcode(10)
    except NotImplementedError:
        pass
    else:
        assert False, 'expected a NotImplemented error for invalid opcode "10"'


def test_program():
    data = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    program(data)
    assert data[0] == 3500, str(data)

    data = [1, 0, 0, 0, 99]
    program(data)
    assert data == [2, 0, 0, 0, 99], str(data)

    data = [2, 3, 0, 3, 99]
    program(data)
    assert data == [2, 3, 0, 6, 99], str(data)

    data = [2, 4, 4, 5, 99, 0]
    program(data)
    assert data == [2, 4, 4, 5, 99, 9801], str(data)

    data = [1, 1, 1, 4, 99, 5, 6, 0, 99]
    program(data)
    assert data == [30, 1, 1, 4, 2, 5, 6, 0, 99], str(data)

test_opcode()
test_program()

if __name__ == '__main__':
    data = load_input()

    pt1 = data.copy()

    # To do this, before running the program, replace position 1 with the
    # value 12 and replace position 2 with the value 2.
    pt1[1] = 12
    pt1[2] = 2

    program(pt1)
    print(f'Result: {pt1[0]}')

    pt2 = data.copy()
    target = 19690720

    for noun in range(0, 100):
        for verb in range(0, 100):
            temp = pt2.copy()

            temp[1] = noun
            temp[2] = verb

            program(temp)
            if temp[0] == target:
                print(f"Found: (100 * {noun}) + {verb} = {(100*noun)+verb}")
