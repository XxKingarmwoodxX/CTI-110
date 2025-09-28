# Antonio Armwood
# 9/28/2025
# P1HW2 CTI-110
# Trip Planner
location = "Texas"
Initial_Budget = 1000
gas = 200
accomodation = 500
food = 200
print ("This program calculates and displays travel expenses")
print ("Enter Budget:", Initial_Budget)
print ("Enter your travel desitnation:", location)
print ("How much do you think you will spend on gas?", gas)
print ("Approximately, how much will you need for accomodation/hotel?", accomodation)
print ("Last, how much do you need for food?", food)


total_expenses = gas + accomodation + food
Remaining_balance = Initial_Budget - total_expenses

print ("------------Travel Expenses------------")
print ("location:","Texas")
print ("Initial Budget:", Initial_Budget)
print ("Fuel:", gas)
print ("Accomodation:", accomodation)
print ("Food:", food)
print ("Remaining balance:", Remaining_balance)

