from replit import clear
from art import logo
print(logo)

#Ask for name input
name = input("What is your name: ")

#Ask for bid price
bid = int(input("How much do you want to bid? $"))

#Add Name and Bid into a dictionary as the key and value
auction_dictionary = {}
auction_dictionary[name]= bid

#Form a while loop to keep the game going till user no longer wants to add others
add_people = True
while add_people:
  players = input("Is there anyone else that would like to play? Yes/No ").lower()
  if players == "yes":
    #Clear the screen
    clear()
    name = input("What is your name?: ")
    bid = int(input("How much do you want to bid?: $"))
    auction_dictionary[name]= bid
  #End game
  elif players == "no":
    add_people = False
    #Find the highest bidder and the amount
    for name in auction_dictionary:
      highest_bidder = max(auction_dictionary, key= auction_dictionary.get)
      highest_amount = auction_dictionary.values()
      highest_amount = max(highest_amount)
      clear()
    print(f"The winner is {highest_bidder} with a bid of ${highest_amount}")