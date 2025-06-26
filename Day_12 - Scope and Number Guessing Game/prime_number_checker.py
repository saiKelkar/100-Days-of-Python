import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    else:
        return True

num = int(input("Enter a whole number: "))
print(f"{num} is prime: {is_prime(num)}")
