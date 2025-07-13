def main():
    expr = input("Expression: ")
    print(expression(expr))

def expression(expr):
    x, y, z = expr.split(" ")
    if y == '+':
        return float(x) + float(z)
    elif y == '-':
        if x > z:
            return float(x) - float(z)
        else:
            return float(z) - float(x)
    elif y == '/':
        if z != 0:
            return format((float(x) / float(z)), ".2f")
        else:
            return "Error"
    elif y == '*':
        return float(x) * float(z)
    else:
        return "Invalid operation"
    
main()