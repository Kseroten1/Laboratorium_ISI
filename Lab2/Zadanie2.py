file = open("C:/Users/23688/Desktop/test.txt", "r")

while True:
    a = file.read()
    special = ['.', ',', '[', ']', '?', '\n']
    b = a
    for i in special:
        b = b.replace(i, "")
    b = b.strip()
    c = list(b.split(" "))
    c = sorted(c, key=len)
    print(c[-1])
    break
