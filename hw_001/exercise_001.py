#! usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    num = input("Введите целое положительное трехзначное число: ")
    num = list(map(int, num))
    print(
        "Сумма цифр: {0}\nПроизведение цифр: {1}".format(
            sum(num), num[0] * num[1] * num[2]
        )
    )
