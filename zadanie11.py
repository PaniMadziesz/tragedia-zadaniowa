a=int(input("podaj pierwszą współrzędną x:"))
b=int(input("podaj drugą współrzędną y:"))

if a>0 and b>0:
    print(f"twój punkt ({a},{b}) lezy na I ćwiartce")
elif a<0 and b>0:
    print(f"twój punkt ({a},{b}) lezy na II ćwiartce")
elif a<0 and b<0:
    print(f"twój punkt ({a},{b}) lezy na III ćwiartce")
elif a>0 and b<0:
    print(f"twój punkt ({a},{b}) lezy na IV ćwiartce")



    # 3,3 I
    # -3, 3 II
    # -3, -3 III
    # 3, -3 IV