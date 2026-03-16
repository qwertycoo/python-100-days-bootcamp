print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

latest_tip = float((tip * bill) / 100)
latest_bill = float((latest_tip +bill) / people)
final_amount = round(latest_bill, 2)
print(f"Each person should pay: ${final_amount}")

