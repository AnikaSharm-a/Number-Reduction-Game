############################################
# Title: Project 4- Loops: 1- Number Reduction Game with Bot
# Programmer: Anika Sharma
# Date: 22/03/2021
# Purpose: To create a 2-player number reduction game with a bot. 
############################################

#imports
from math import floor
from random import choice

#rules of the game
print("Welcome to the 2-player number reduction game! \n \n"
"The rules of the game are:"
"\n \t1. The first player to write a 0 wins."
"\n \t2. To start the game, Player 1 picks any whole number greater than 1"
"\n \t3. The players take turns reducing the number by either: \n \t \ta. Subtracting 1 from the number your opponent just wrote, \tOR \n \t \tb. Halving the number your opponent just wrote. \n \n")

#player tracker and initial number input
player = "Player 1,"
number = int(input(player + " enter the starting whole number [must be greater than 1]: "))

#to make them input a number greater than 1
while number == 0 or number == 1:
  print("Please enter a whole number greater than 1. \n")
  number = int(input(player + " enter the starting whole number [must be greater than 1]: "))

print('')

#while the number is not reduced to 0
while number != 0:

  #to switch the player each time
  if player == "Player 1,":
    player = "Bot,"
  else:
    player = "Player 1,"
  
  #the two choices math
  choice1 = number - 1
  choice2 = floor(number / 2)
  
  #if the only choice is 1
  if choice1 == 1 and choice2 == 1:
    print(player, "your only choice is 1")
    number = 1

  #if the only choice is 0
  elif choice1 == 0 and choice2 == 0:
    print(player, "your only choice is 0. You win!")
    break

  #if the choices are not 1 or 0 yet
  else:
    
    #if it is the bot's turn
    if player == "Bot,":
      print("The choices for the bot are:", choice1, "or", choice2)
      
      #if one of the choices are 2- always pick 2
      if choice1 == 2 or choice2 == 2:
        number = 2
        print("The Bot chose 2")

      #if one of the choices is 5, 4, 3, pick the other option
      elif choice1 in [5, 4, 3]:
        number = choice2
        print("The Bot chose", str(number))

      elif choice2 in [5, 4, 3]:
        number = choice1
        print("The Bot chose", str(number))

      #if the choices are greater than or equal to 6, pick randomly
      elif choice1 >= 6 or choice2 >= 6:
        number = choice([choice1, choice2])
        print("The Bot chose", str(number))

    #if it is the player's turn
    elif player == "Player 1,":
      number = int(input(player + " your choices are " + str(choice1) + " or " + str(choice2) + ": "))

    #if the player inputs an invalid number
    while number != choice1 and number != choice2:
      print("You have given an invalid number. Please try again. \n")
      number = int(input(player + " your choices are " + str(choice1) + " or " + str(choice2) + ": "))
  
  print('')

#final winning output
print("\n \n***" + player.replace(",", ""), "wins***"
"\n \nEnd of program")