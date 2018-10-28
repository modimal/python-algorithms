#! usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    chr_num = int(input("Введите номер буквы в алфавите: "))
    print("Буква под номером {}: {}".format(chr_num, chr(chr_num + 96)))
