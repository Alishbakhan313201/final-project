import random

print("create strong passwords")

charecters=("abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890 ~!@#$%^&*()_+><';[]?/")
number=input('amount of passwords generate:')
number=int(number)

lenght=input("enter your passwords lenght:")
lenght=int(lenght)

print(" your Passwords is redy ")
for pwd in range (number):
    password=''

for c in range (lenght):
    password += random.choice(charecters)

    print(password) 