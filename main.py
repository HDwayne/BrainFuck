def convert(string: str) -> list:
    list1 = []
    list1[:0] = string
    return [x for x in list1 if x in ["<", ">", "+", "-", ".", ",", "[", "]"]]


def increment_p(pointer: int) -> int:  # >
    if pointer + 1 > array_size - 1:
        print("POINTER OUT OF BOUNDS")
        exit()
    return pointer + 1


def decrement_p(pointer: int) -> int:  # <
    if pointer - 1 < 0:
        print("POINTER OUT OF BOUNDS")
        exit()
    return pointer - 1


def increment_v(pointer: int, array: list):  # +
    if array[pointer] + 1 > 255:
        print("INCORRECT VALUE")
        exit()
    array[pointer] += 1


def decrement_v(pointer: int, array: list):  # -
    if array[pointer] - 1 < 0:
        print("INCORRECT VALUE")
        exit()
    array[pointer] -= 1


def output_v(pointer: int, array: list):  # .
    print(chr(array[pointer]), end='')


def accept(integer: int, pointer: int, array: list):  # ,
    array[pointer] = integer


def jump(pointer: int, pos: int, array: list, prog: list) -> int:  # [
    if array[pointer] == 0:
        nbother = 0
        pos += 1
        while not (prog[pos] == "]" and nbother == 0):
            if prog[pos] == "[":
                nbother += 1
            if prog[pos] == "]":
                nbother -= 1
            pos += 1
        return pos + 1
    return pos


def back(pointer: int, pos: int, array: list, prog: list) -> int:  # ]
    if array[pointer] != 0:
        nbother = 0
        pos -= 1
        while not (prog[pos] == "[" and nbother == 0):
            if prog[pos] == "]":
                nbother += 1
            elif prog[pos] == "[":
                nbother -= 1
            pos -= 1
        return pos
    return pos


def verif(all_prog: list) -> bool:
    cpt1 = 0
    cpt2 = 0
    for prog in all_prog:
        for elem in prog:
            if elem == "[":
                cpt1 += 1
            elif elem == "]":
                cpt2 += 1
    return cpt1 == cpt2


nb_brainfuck = int(input("program line count : "))
array_size = int(input("Size of the array : "))
nb_integer = int(input("number of integer input to the Brainfuck program : "))


prog_brainfuck = []
integer_input = []

print("Brainfuck prog :")
for i in range(nb_brainfuck):
    r = input()  # brainfuck prog
    prog_brainfuck += convert(r)

if nb_integer != 0:
    print("Input :")
    for i in range(nb_integer):
        c = int(input())  # integer input
        integer_input.append(c)

print("Output :")
pointer = 0
pos_integer = 0
array = [0] * array_size

if verif(prog_brainfuck):
    i = 0
    while i < len(prog_brainfuck):
        if prog_brainfuck[i] == ">":
            pointer = increment_p(pointer)
        elif prog_brainfuck[i] == "<":
            pointer = decrement_p(pointer)
        elif prog_brainfuck[i] == "+":
            increment_v(pointer, array)
        elif prog_brainfuck[i] == "-":
            decrement_v(pointer, array)
        elif prog_brainfuck[i] == ".":
            output_v(pointer, array)
        elif prog_brainfuck[i] == ",":
            accept(integer_input[pos_integer], pointer, array)
            pos_integer += 1
        elif prog_brainfuck[i] == "[":
            i = jump(pointer, i, array, prog_brainfuck)
        elif prog_brainfuck[i] == "]":
            i = back(pointer, i, array, prog_brainfuck)
        i += 1
else:
    print("SYNTAX ERROR")
    exit()
    