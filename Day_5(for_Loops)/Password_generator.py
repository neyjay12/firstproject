import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbol = ['!','£','$','%','&','*','(',')','+']

print("Welcome to Python Password Generator")
nr_letters = int(input("How many letters would you like to generate? "))
nr_numbers = int(input("How many numbers would you like to generate? "))
nr_symbols = int(input("How many symbols would you like to generate? "))


password = []

for char in range(1, nr_letters + 1):
    password += random.choice(letters)


for num in range(1, nr_numbers + 1):
    password += random.choice(numbers)

for sym in range(1, nr_symbols + 1):
    password += random.choice(symbol)

password_str = list(password)
random.shuffle(password_str)
shuffled_password = "".join(password_str)
print(shuffled_password)