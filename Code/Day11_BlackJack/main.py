import random
from replit import clear
from art import logo


def deal_card():
  """Returns a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(card_list):
  """Takes a list of cards and return the score of all the cards"""
  return sum(card_list)
  if sum(card_list) ==21 and len(card_list) ==2:
    return 0
  elif 11 in card_list and sum(card_list) > 21:
    card_list.remove(11)
    card_list.append(1)

def compare(user_score, computer_score):
  """Compares the user_score and computer_score"""
  if computer_score == user_score:
    return "Draw"
  elif computer_score == 0:
    return "Computer has blackjack. You lose"
  elif user_score == 0:
    return "You have a blackjack. You win!"
  elif user_score > 21:
    return "You went over you have lost"
  elif computer_score > 21:
    return "Computer went over. You win!"
  elif user_score > computer_score:
    return "You have a higher score, you win!"
  else:
    return "Computer has a higher score, you lose"

def play_game():
  
  print(logo)
  
  computer_cards = []
  user_cards = []
  game_over = False

  for x in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"  Your cards: {user_cards}, current score: {user_score}")
    print(f"  Computers first card: {computer_cards[0]}")

    if user_score == 0 or computer_score ==0 or user_score>21:
      game_over = True
    elif input("Would you like do draw another card? Type 'y' or 'n': ") == 'y':
      user_cards.append(deal_card())
      calculate_score(user_cards)
    else:
      game_over = True
    
  while computer_score != 0 and computer_score< 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Computer's final cards: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
  



## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

