import random
print('welcome to your password generator')
chars='abcdefghijklmnopqrstuvwxyz!@#$%^&*0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number=input('amount of password to generate')
number=int(number)
length=input('your password length:')
length=int(length)
print('/here are your passwords:')
for pwd in range (number):
    passwords=''
    for c in range(length):
        passwords +=random.choice(chars)
    print(passwords)    
