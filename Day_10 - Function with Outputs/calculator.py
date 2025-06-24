'''
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error"
'''
    
def operation(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            return "Error"
    else:
        return "Error in operator"
    
num_1 = float(input("Enter a number: "))
operator = input("Enter an operator: +\n -\n *\n /\n")
num_2 = float(input("Enter another number: "))

print(operation(num_1, num_2, operator))

