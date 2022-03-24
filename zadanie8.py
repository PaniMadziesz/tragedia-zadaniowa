#!/usr/bin/python
import random


a=int(input("podaj pierwszą liczbę z zakresu:"))
b=int(input("podaj drugą liczbę z zakresu:"))

for i in range(6):
    print(random.randint(a,b))

#pyton liczy od 0 a nie od 1