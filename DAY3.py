print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      ''')
print('Welcome to Tresure Island.')
print('Your mission is to find the treasure.')
direction = str(input('You\'re at a crossroad, where do you want to go? Left or Right.')).lower()[0]
if direction == 'l':
    choice = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat or "swin" to swin across:').lower()[0]
    if choice == 'w': 
        doors = str(input('You arrive at the island unharmed. There is a house with 3 doors.One red, one yellow and one blue. Which colour do you choose?')).lower()[0]
        if doors == 'r':
            print('You found the trasure! YOUWIN!')
        elif doors == 'y' or doors == 'b':
            print('You enter a room of beasts. GAME OVER.')
        else:
            print("You enter a door that doesn't exist. GAME OVER!!")
    else:
        print('You got attacked by an angry trout. GAME OVER!!!')
        
else:
    print('You fell into a hole, Game over!!!')