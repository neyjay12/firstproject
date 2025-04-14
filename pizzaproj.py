print("Welcome to the Pizza Delivery Services!.")
size = input("What size pizza do you want? S,M or L: ")
pepperoni = input("What pepperoni do you want? Y or N : ")
extra_cheese = input("Do you want extra cheese? Y or N : ")

bill = 0

if size == "L" or size == "l":
    bill = bill + 25
elif size == "M" or size == "m":
    bill = bill + 20
elif size == "S" or size == "s":
    bill = bill +15
else:
    print("Please enter a valid size.")

if pepperoni == "Y" or pepperoni == "y":
    if size == "S" or size == "s":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y" or extra_cheese == "y":
    bill = bill + 1

print(f"Your bill is ${bill}")
