def main():
    mass = int(input("m: "))
    einstein(mass)

def einstein(mass):
    c = 300000000
    print(f"E: {mass * c * c}")

main()