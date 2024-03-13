import string
import random

f = open('C:/Users/23688/Desktop/passwords.txt', "w")
for i in range(1000):
    a = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    f.write(a)
    f.write("\n")
f.close()
