import random

computer_choice = random.choice(['rock', 'paper', 'scissors'])

# print(computer_choice)

print("Welcome to the Rock, paper, scissors game!")

user1 = input("Type 0 for Rock, 1 for Paper, 2 for Scissors: ")

if user1 == '0' and computer_choice == 'rock':
    print(f"Computer chose {computer_choice}")
    print("Its a Draw!")
elif user1 == '0' and computer_choice == 'paper':
    print(f"Computer chose {computer_choice}")
    print("You loose!")
elif user1 == '0' and computer_choice == 'scissors':
    print(f"Computer chose {computer_choice}")
    print("You win!")
elif user1 == '1' and computer_choice == 'rock':
    print(f"Computer chose {computer_choice}")
    print("You win!")
elif user1 == '1' and computer_choice == 'paper':
    print(f"Computer chose {computer_choice}")
    print("Its a Draw!")
elif user1 == '1' and computer_choice == 'scissors':
    print(f"Computer chose {computer_choice}")
    print("You loose!")
elif user1 == '2' and computer_choice == 'rock':
    print(f"Computer chose {computer_choice}")
    print("You loose!")
elif user1 == '2' and computer_choice == 'paper':
    print(f"Computer chose {computer_choice}")
    print("You win!")
elif user1 == '2' and computer_choice == 'scissors':
    print(f"Computer chose {computer_choice}")
    print("Its a Draw!")
else:
    print("Invalid choice!")