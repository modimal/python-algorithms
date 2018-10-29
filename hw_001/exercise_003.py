#! usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    """
    По введенным пользователем координатам двух 
    точек вывести уравнение прямой, проходящей через эти точки.
    """

    print("\nВведите координаты 1-ой точки.")
    x1, y1 = float(input("x1: ")), float(input("y1: "))
    print("\nВведите координаты 2-ой точки.")
    x2, y2 = float(input("x2: ")), float(input("y2: "))

    try:
        k = (y2 - y1) / (x2 - x1)
        b = (x2 * y1 - y2 * x1) / (x2 - x1)
    except ZeroDivisionError as err:
        print("\nERROR:", err)
    else:
        k = int(k) if k.is_integer() else k
        b = int(b) if b.is_integer() else b

        print("Уравнение прямой: y = {0}x {2} {1}".format(k, b if b > 0 else abs(b), "+" if b > 0 else "-"))
