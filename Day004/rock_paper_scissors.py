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

gameChoices = [rock, paper, scissors]
playerChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
compChoice = random.randint(0,len(gameChoices)-1)

if playerChoice < 0 or playerChoice > 2:
    print("You typed an invalid number")
else:
    print(gameChoices[playerChoice])
    print(f"\n\nComputer chose: {compChoice}")
    print(gameChoices[compChoice])

    if compChoice == 2 and playerChoice == 0:
        print("\n\nYou win! :)")
    elif playerChoice == 2 and compChoice == 0:
        print("\n\nYou lose :(")
    elif compChoice == playerChoice:
        print("\n\nIt's a draw")
    elif compChoice < playerChoice:
        print("\n\nYou win! :)")
    else:
        print("\n\nYou lose :(")