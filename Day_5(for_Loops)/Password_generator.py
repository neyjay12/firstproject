import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbol = ['!','£','$','%','&','*','(',')','+']

print("Welcome to Python Password Generator")
nr_letters = int(input("How many letters would you like to generate? "))
nr_numbers = int(input("How many numbers would you like to generate? "))
nr_symbols = int(input("How many symbols would you like to generate? "))

#Easy choice
password = ""

for char in range(0, nr_letters):
    password += random.choice(letters)

for num in range(0, nr_numbers):
    password += random.choice(numbers)

for sym in range(0, nr_symbols):
    password += random.choice(symbol)

print(password)


#Hard level: Where the password is mixed randomly

password_list = []

for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for num in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

for sym in range(0, nr_symbols):
    password_list.append(random.choice(symbol))

print(f'Your old password is : {password_list}')
random.shuffle(password_list)
print(f'Your shuffled password is {password_list}')

password = "".join(password_list)
print(f"Your new password is: {password}")
