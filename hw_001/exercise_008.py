#! usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    """
    Определить, является ли год, который ввел пользователем, високосным или невисокосным.
    """

    year = int(input("Введите год: "))

    if year % 4 == 0 and (not year % 100 == 0 or (year % 100 == 0 and year % 400 == 0)):
        print("Год високосный.")
    else:
        print("Год невисокосный.")
