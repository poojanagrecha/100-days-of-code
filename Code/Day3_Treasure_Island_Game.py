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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

step1 = input("You're at a crossroad. Would you like to go left or right? ").lower()
print(step1)
if step1 == "left":
  swim_wait= input("You've come to a lake. Would you like to swim or wait? ")
  print(swim_wait)
  if swim_wait == "wait":
    door = input("You have seen a multidoored house. Which door would you like to enter? Blue, Red, or Yellow? ")
    print(door)
    if door == "yellow":
      print("You win the big ole box of gold treasure!")
    elif door == "red":
      print("Burned by fire. Game over")
    elif door == "blue":
      print("Eaten by beasts. Game Over")
    else:
      print("Game Over.")
  else:
    print("You have been attacked by a vicious trout! Game over")
else:
  print("You have fallen into a hole. Game over")