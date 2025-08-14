# project 3. HOW MUCH BILL TO BE PAID WITH TIP
# Challenge --->
# 1. todo : work out how much they need to pay by size .
# 2. todo : work out how much they need to pay by with the pepperoni.
# 3. todo : work out how much they need to pay by with the extra cheese.


print("Welcome to the Pizza Deliveries !!!")
size = input("What size of pizza u wanna pick ? S, M, or L : ")
pepperoni = input("Do u wanna add pepperoni to add up up ? Y or N : ")
extra_cheese = input("Do u wanna add extra cheese ?  Y or N : ")
bill = 0

# 1. todo : work out how much they need to pay by size .

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
    
else:
    print("You typed the wrong inputs.")

# 2. todo : work out how much they need to pay by with the pepperoni.

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3


# 3. todo : work out how much they need to pay by with the extra cheese.

if extra_cheese == "Y":
    bill += 1
    
    
    
print(f"Your final bill is :  ${bill}.")