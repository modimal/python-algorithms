#! usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    """
    Все побитовые операции применяются к паре битов.
    Побитовое ИЛИ.
    Если оба бита равны 0, тогда результат равен 0, 
    иначе равен 1.
    """
    print("\nПобитовое ИЛИ: {0}.".format(5 | 6))

    """
    Побитовое И.
    Если оба бита равны 1, тогда результат равен 1,
    иначе равен 0.
    """
    print("Побитовое И: {0}.".format(5 & 6))

    """
    Исключающее ИЛИ.
    Если олин из битов равен 1, тогда результат равен 1,
    иначе равен 0.
    """
    print("Исключающее ИЛИ: {0}.".format(5 ^ 6))

    """
    Побитовое отрицание.
    Инвертирует все биты операнда.
    Питон использует бесконечные биты и дополняет 
    единицами слева. Как я понял, лидирующие нули 
    у инвертированного числа он заменяет на 1, 
    чтобы сохранить длину числа.
    """
    print("Побитовое отрицание: 5: {0}, 6: {1}".format(~5, ~6))

    """
    Побитовый сдвиг влево.
    Сдвигает биты на N битов влево, 
    начиная с младшего бита. Пустые места после 
    сдвига заполняются нулями.
    """
    print("Побитовый сдвиг влево на 3 бита: 5: {0}, 6: {1}.".format(5 << 3, 6 << 3))

    """
    Побитовый сдвиг вправо.
    Делает обратное сдвигу влево.
    """
    print("Побитовый сдвиг вправо на 3 бита: 5: {0}, 6: {1}.".format(5 >> 3, 6 >> 3))
