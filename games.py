
import random   

print("Welcome to Rock, Paper, Scissors Game")
print("1. Rock\n2. Paper\n3. Scissors")

player_choice = int(input("Enter the number: "))

# Player choice
if player_choice == 1:
    player_choice = "stone"
elif player_choice == 2:
    player_choice = "paper"
elif player_choice == 3:
    player_choice = "scissors"
else:
    print("Invalid number")
    exit()   

# Computer choice
computer_choice = random.randint(1, 3)

if computer_choice == 1:
    computer_choice = "stone"
elif computer_choice == 2:
    computer_choice = "paper"
else:
    computer_choice = "scissors"

print("Player choice:", player_choice)
print("Computer choice:", computer_choice)


if player_choice == computer_choice:
    print("Match is Tie")
elif (player_choice == "stone" and computer_choice == "scissors") or \
     (player_choice == "paper" and computer_choice == "stone") or \
     (player_choice == "scissors" and computer_choice == "paper"):
    print("You Win!")
else:
    print(" Computer Wins")



 





