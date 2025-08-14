# 2. Bill and Tip Calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("How much amount of tip would u like to give? 10, 12, 15- "))
people = int(input("How many people to splot the bill? "))

# bill_with_tip = bill * (1 + tip / bill)
# print("Your Bill with the tip is : ", bill_with_tip)

tip_as_percent = tip / 100
total_tip = bill * tip_as_percent
total_bill = bill + total_tip

bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print (f"Each person should pay ${final_amount} ")