print("Welcome to the tip calculator!")

# asking for user input to get the required data
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# calculate total_bill
total_bill = bill + ((bill * tip)/100)
# calculate payment made by each person
payment = total_bill / people

# :.2f to format the output to exactly two decimal places
print(f"Each person should pay: ${payment:.2f}")
