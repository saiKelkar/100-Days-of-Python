# Dictionaries:
# {key: value}
# {"Bug": "An error in a program that prevents the program from running as expected."}

# if more than one item in a dictionary
'''
{
    "Bug": "An error",
    "Function": "A piece of code that you can call over and over again",
    "Loop": "Action of doing something over and over again"
}
'''

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again",
    "Loop": "The action of doing something over and over again",
}

# To retrieve an item from the dictionary
print(programming_dictionary["Bug"])

# To add a piece of entry 
programming_dictionary["Control Statements"] = "A programming construct that alters the sequential flow of execution, enabling decision-making and repition based on condition"
print(programming_dictionary)

# Create an empty dictionary
empty_dictionary = {}

# Wipe an exisiting dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key) # Prints the keys
    print(programming_dictionary[key]) # Prints the values