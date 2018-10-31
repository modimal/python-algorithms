#! usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from string import ascii_lowercase as al

if __name__ == "__main__":
    """
    Написать программу, которая генерирует в указанных пользователем границах:
    случайное целое число;
    случайное вещественное число;
    случайный символ. Для каждого из трех случаев пользователь задает 
    свои границы диапазона. Например, если надо получить случайный 
    символ от 'a' до 'f', то вводятся эти символы. Программа должна 
    вывести на экран любой символ алфавита от 'a' до 'f' включительно.
    """

    print("\nВведите диапозон целых или вещественных чисел, или символов.")
    start, end = input("От: "), input("До: ")

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
