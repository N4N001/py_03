list=[1, 2, 3, 4, 5, 6]
a=int(input("Jaké císlo chcete vyhledávat? "))
if a in list:
    print(a, "je v listu")
else:
    print(a, "není v listu")
input("Stiskni klávesu ENTER pro ukončení programu")