a=int(input("podaj długość pierwszeo boku:"))
b=int(input("podaj długość drugiego boku:"))
c=int(input("podaj długość trzeciego boku:"))
if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0:
    print("taki trjkójkąt morzna zbudować")
else:
    print("takiego trójkąta nie mona zbudować")