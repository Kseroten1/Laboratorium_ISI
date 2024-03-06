import random
a = random.randint(1, 100)
c = 0
notEnd = True
while notEnd:
    b = int(input("Podaj liczbe\n"))
    c += 1
    if b == a:
        print("Gratulacje uzytkowniku wygrales iphona! Liczba prób: ", c)
        notEnd = False
    elif b > a:
        print("Liczba ktorej szukasz jest mniejsza")
    else:
        print("liczba ktorej szukasz jest wieksza")
