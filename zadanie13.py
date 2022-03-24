#!/usr/bin/python
import random

liczba=(random.randint(1,20))
proby=[]

a=int(input("jaka liczba została wylosowana"))
proby.append(a)

if a==liczba:
    print("zgadłeś za pierwszym razem")
else:
    while a!=liczba:
        proby.append(a)
        int(input("próbuj kolejny raz"))
        
        print(f"trfiłeś za {len(proby)} razem")