print("Welcome to the roller coaster!")

height = int(input("What is your height in CM? "))
bill = 0

if height >= 120:
    print("You ca ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Child tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")

    wants_photo = input("Do you want a photo take type y for Yes and n for No")
    if wants_photo == "y":
        bill += 3

    print(f"Your total bill is ${bill}")

else:
    print("You are too short to take this rollercoaster!")