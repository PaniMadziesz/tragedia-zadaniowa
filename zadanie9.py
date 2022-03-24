waga=float(input("podaj swoją wagę:"))
wzrost=float(input("podaj swój wzrost:"))

BMI=(waga/(wzrost)**2)

if BMI<20:
    print("Niedowaga")
elif 20<BMI<25:
    print("Prawidłowa waga")
elif 25<BMI<30:
    print("Niedwaga")
else:
    print("Otyłość")