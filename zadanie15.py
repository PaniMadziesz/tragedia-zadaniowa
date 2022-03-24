import random

lu=0
lk=0

wybory=["papier", "kamień", "nozyce"]

losk=random.choice(wybory)
losu=input("papier, kamień, nozyce")

if lu=="papier" and lk=="papier":
    print("Remis")
elif lu=="kamień" and lk=="kamień":
    print("Remis")
elif lu=="nozyce" and lk=="nozyce":
    print("Remis")
elif lu=="papier" and lk=="kamień":
    print("Wygrałeś")
elif lu=="papier" and lk=="nozyce":
    print("Przegrałeś")
elif lu=="kamien" and lk=="papier":
    print("Przegrałeś")
elif lu=="kamień" and lk=="nozyce":
    print("wygrałeś")
elif lu=="nozyce" and lk=="papier":
    print("Wygrałeś")
else lu=="nozyce" and lk=="kamień":
    print("Przegrałeś") 