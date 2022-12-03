#!/usr/bin/env python3
#-*- coding: utf-8 -*-
if __name__ == '__main__':
    s = input("Введите преложение: ")
    words = s.split()
    print(min(words, key=len))