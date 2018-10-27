#! usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    char_1, char_2 = input("Введите две буквы (a, z): ").split(", ")
    print(
        "место буквы {}: {}; место буквы {}: {}; количество букв между ними: {}.".format(
            char_1,
            ord(char_1) - 96,
            char_2,
            ord(char_2) - 96,
            abs(ord(char_1) - ord(char_2)) - 1,
        )
    )
