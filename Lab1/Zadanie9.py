a = input()
a = a.replace(" ", "")
b = a[::-1]

if a == b:
    print("Tak, to palindrom")
else:
    print("Nie, to nie palindrom")
