print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`." ` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print('''
Welcome to Treasure Island.
your mission is to find the treasure.
You're at a crossroad. Where do you want to go?
''')

inputChoice = input('     Type "left" or "right"\n')

if inputChoice.upper() == "LEFT":
    print("You've come to a lake. There is an island in the middle of the lake.")
    inputChoice = input('     Type "wait" to wait for a boat. Type "swim" to swim across.\n')

    if inputChoice.upper() == "WAIT":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        inputChoice = input('     One red, one yellow and one blue. Which colour do you choose?\n')

        if inputChoice.upper() == "YELLOW":
            print("You found the treasure! You Win!")
        elif inputChoice.upper() == "RED":
            print("You are burned by fire! Game Over.")
        elif inputChoice.upper() == "BLUE":
            print("You are eaten by beasts! Game Over.")
        else:
            print("Game Over.")

    else:
        print("You are attacked by trout. Game Over.")
else:
    print("You fall into a hole. Game Over.")