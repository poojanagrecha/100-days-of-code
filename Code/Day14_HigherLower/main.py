import random
import art
from replit import clear
from game_data import data

print(art.logo)
score = 0
b = random.choice(data)
continue_game = True
while continue_game:
  a = b
  a_name = a["name"]
  a_desc = a["description"]
  a_country = a["country"]
  a_followers = a["follower_count"]
  print(f"Compare A: {a_name}, a {a_desc}, from {a_country}")
  print(art.vs)
  b = random.choice(data)
  while a == b:
    b = random.choice(data)
  b_name = b["name"]
  b_desc = b["description"]
  b_country = b["country"]
  b_followers = b["follower_count"]
  print(f"Against B: {b_name}, a {b_desc}, from {b_country}")

  user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  clear()
  print(art.logo)

  if user_guess == 'a' and a_followers > b_followers:
    score +=1
    print(f"You're correct! Current score: {score}")
  elif user_guess == 'b' and b_followers > a_followers:
    score +=1
    print(f"You're correct! Current score: {score}")
  else:
    print(f"Incorrect. You lose. Your final score is: {score}")
    continue_game = False