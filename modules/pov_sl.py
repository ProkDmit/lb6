#!/usr/bin/env python3
#-*- coding: utf-8 -*-
s=input("Введите преложение: ")
words=s.split()
print(min(words, key=len))