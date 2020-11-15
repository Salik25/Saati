from numpy import round
from numpy import ones


def vector(matrix):
    vect = matrix[:, 0]
    vec = vect / vect.sum()
    return vec


count = int(input("Кол-во критериев:  "))

chisla = set(i for i in range(1, 10))

matr = ones([count, count])
for vert in range(0, count):
    for hor in range(0, count):
        if vert < hor:
            a = str(
                input(f'На сколько важен критерий {vert} относительно критерия {hor}? Ввести по 10 бальной шкале: '))
            if a.isdigit() and float(a) in chisla:  # error handling
                matr[vert, hor] = float(a)
                matr[hor, vert] = 1 / float(a)

kriterii = vector(matr)
for vert in range(len(kriterii)):
    print(f'{vert} критерий  = {round(kriterii[vert], 2)}')
