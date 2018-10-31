#! usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    """
    Вводятся три разных числа. Найти, какое из них 
    является средним (больше одного, но меньше другого).
    """

    print("\nВведите три разных числа (целое или с плавающей точкой):")
    a, b, c = float(input("a: ")), float(input("b: ")), float(input("c: "))

    if b > a > c or c > a > b:
        print("Среднее число: {}".format(int(a) if a.is_integer() else a))
    elif a > b > c or c > b > a:
        print("Среднее число: {}".format(int(b) if b.is_integer() else b))
    else:
        print("Среднее число: {}".format(int(c) if c.is_integer() else c))
