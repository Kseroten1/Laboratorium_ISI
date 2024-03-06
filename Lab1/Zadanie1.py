a = input()
b = ""
for i in range(len(a)):
    b += a[len(a) - i - 1]
print(b)

# opcja 2

b = a[::-1]
print(b)
