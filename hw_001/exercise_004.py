#! usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from string import ascii_lowercase as al

if __name__ == "__main__":
    start, end = input(
        "Введите диапозон целых или вещественных чисел, или символов.\n"
        "Примеры: -30 - -10 или 1.05 - 5.3 или a - f.\nВвод: "
    ).split(" - ")

    try:
        rand_num = random.randint(int(start), int(end))
        print("Случайное целое число: {}".format(rand_num))
        exit(0)
    except ValueError:
        pass

    try:
        rand_num = random.uniform(float(start), float(end))
        print("Случайное число с плавающей точкой: {}".format(rand_num))
    except ValueError:
        letters = al[al.find(start):al.rfind(end) + 1]
        rand_chr = random.choice(letters)
        print("Случайная буква: {}".format(rand_chr))
