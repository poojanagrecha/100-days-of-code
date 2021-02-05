#Create a Tip Calculator
print("Welcome to the tip calculator.")
#Create inputs and convert them to respective data type
total = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))
bill = total/split * (tip/100 + 1)
#Round the final result
final_result = round(bill, 2)
#Have the final result show 2 decimal places
final_result = "{:.2f}".format(bill)
print(f'Each person should pay ${final_result}')