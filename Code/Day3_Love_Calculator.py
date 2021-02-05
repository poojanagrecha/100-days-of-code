# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

fullname = name1.lower() + name2.lower()

# print(fullname)

score_true = fullname.count("t") + fullname.count("r") + fullname.count("u") + fullname.count("e")

score_love = fullname.count("l") + fullname.count("o") + fullname.count("v") + fullname.count("e")

final_score = str(score_true) + str(score_love)
final_score = int(final_score)
# print(final_score)

if (final_score <10) or (final_score >90):
  print(f"Your score is {final_score}, you go together like coke and mentos.")
elif (final_score >=40) and (final_score <=50):
  print(f"Your score is {final_score}, you are alright together.")
else:
  print(f"Your score is {final_score}.")
