import random

liczbyK=[]
liczbyU=[]

for i in range (6):
    liczba=(random.randint(1,50))
    liczbyK.append(liczba)
    b=int(input(f"podaj liczbe {i+1 } z 50:"))
    while b>50 or b<1:
        print("podaj liczbe od 1 do 50")
        b=int(input(f"podaj liczb {i+1} z 6:"))
    liczbyU.append(b)

print("wylosowane liczby")
print(*liczbyK, sep=',')
print("twoje liczby")
print(*liczbyU, sep=',')

trafione=set(liczbyK)&set(liczbyU)

if len(trafione)>0:
    print(f"trafiłeś {len(trafione)} z 6 liczb: {trafione}")
else:
    print("nie zgadłeś zadnej z liczb")
        

#for i in range (6):
    #liczba=int(input("podaj liczbę od 1 do 50"))
    #liczbyU.append(liczba)


#if liczba>50 or liczba<1:
    #print("twoje liczby nie są z tego przedziału co powinny być")
#else:
    #liczbyU.append(liczba)

