import random
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "@#$%&*"
numbers = "0123456789"

print("Welcome to PyPassword Generator!")

num_letters = int(input("How many letters would you like in your password? \n"))
num_symbols = int(input("How many symbols would you like? \n"))
num_numbers = int(input("How many numbers would you like? \n"))

password_letters = [random.choice(letters) for _ in range(num_letters)]
password_symbols = [random.choice(symbols) for _ in range(num_symbols)]
password_numbers = [random.choice(numbers) for _ in range(num_numbers)]

password_list = password_letters + password_symbols + password_numbers
print(password_list)
random.shuffle(password_list)

password = "".join(password_list)

print(f"Your password is {password}")