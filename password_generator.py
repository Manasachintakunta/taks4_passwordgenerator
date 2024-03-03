import random
import string
def gen_password(length):
    c=string.ascii_letters +string.digits
    password=''.join(random.choice(c) for i in range(length))
    return password
print("enter length of the password")
length=int(input())
p=gen_password(length)
print(f" Your password: {p}")
