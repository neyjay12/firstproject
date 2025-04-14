from random import choice

print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
choice1 = input("You're at the cross road. Where do you want to go? Type 'left' or 'right': ").lower()

if choice1 == 'left':
    choice2 = input("You have come to a lake there is an island in the middle of the lake would you like to 'swim' or 'wait' : ").lower()
    if choice2 == 'wait':
        choice3 = input("Your patience has led you to door three (3) doors, which door would you like to choose 'red', 'blue' or 'yellow': ").lower()
        if choice3 == 'yellow':
            print('Congratulations! You win!')
        elif choice3 == 'red':
            print('Sorry, you lose!')
        elif choice3 == 'blue':
            print('Sorry, you lose!')
        else:
            print('Invalid input. Please try again.')
    elif choice2 == 'swim':
        print("Game over the sharks ate you!")
    else:
        print("Invalid input. Please try again.")


elif choice1 == 'right':
    print("Game over as you fell into a hole")
else:
    print("Invalid input")

