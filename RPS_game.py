print("welcome to Rock, Paper and scissors!")
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
Player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
Computer_choice = random.randint(0, 2)
print(f"Computer chose {Computer_choice}")

if Player_choice == "0" and Computer_choice == 2:
    print(f"You chose {rock} and the computer chose {scissors}. You lost!")
elif Player_choice == "1" and Computer_choice == 0:
    print(f"You chose {paper} and the computer chose {rock}. You win!")
elif Player_choice == "2" and Computer_choice == 1:
    print(f"You chose {scissors} and the computer chose {paper}. You win!")
elif Player_choice == "1" and Computer_choice == 2:
    print(f"You chose {paper} and the computer chose {scissors}.You lost")
elif Player_choice == 2 and Computer_choice == 0:
    print(f"You chose {scissors} and the computer chose {rock}. You lost!")
elif Player_choice == Computer_choice:
    print(f"You both choose the same hence it is a draw")
else:
    print("You choose a invalid number. You lose!")
