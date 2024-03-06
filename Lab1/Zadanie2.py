a = input()
b = ""
for i in range(len(a)):
    if a[i] == 'o':
        b += '0'
    elif a[i] == 'e':
        b += '3'
    elif a[i] == 'i':
        b += '1'
    elif a[i] == 'a':
        b += '4'
    else:
        b += a[i]
print(b)

# opcja 2

a = a.replace('o', '0')
a = a.replace('e', '3')
a = a.replace('i', '1')
a = a.replace('a', '4')
print(a)
