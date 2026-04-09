#This is my version of tip cal.
print("Welcome to the tip calculator!")
Total_bill=float(input("What was your total bill: $"))
percentage_of_bill=int(input("How much % of bill would you like to pay? 10  15  20?: $"))
Amount=float((percentage_of_bill/100)*Total_bill+Total_bill)
split_bill=int(input("How many people to split the bill: "))
final_tip=round(Amount/split_bill,2)
print(f"Each person should pay: ${final_tip}")

#this is angela yu's version of tip cal.

print ("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage of tip would you like to give? $"))
people = int(input("How many people to split the bill? "))
tip_as_percent = (tip/100)
total_tip_amount = (bill*tip_as_percent)
total_bill = (bill+ total_tip_amount)
bill_per_person = (total_bill/people)
final_amount = round(bill_per_person,2)
print(f"Each person should pay: ${final_amount}")