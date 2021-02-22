#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == 'easy':
    return EASY_ATTEMPTS
  else:
    return HARD_ATTEMPTS


def compare(answer, number, attempts):
  if answer == number:
      print("Correct answer!")
  elif answer > number:
    print("Too high")
    return attempts - 1
  elif number > answer:
    print("Too low")
    return attempts - 1

def game():
  print(logo)
  print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")
  number = random.randint(1,101)
#   print(f"Psst the correct answer is {number}")
  attempts = difficulty()
  answer = 0
  while answer != number:
    print(f"You have {attempts} attempts remaining to guess the number.")
    answer = int(input("Make a guess: "))
    attempts = compare(answer, number, attempts)
    if attempts == 0:
      print(f"You've run out of guesses, you lose. The correct answer was {number}")
      return
game()