def main():
    greeting = input("Greeting: ")
    user_greeting(greeting)

def user_greeting(greeting):
    if greeting.lower().startswith("h"):
        if greeting.startswith("hello"):
            print("$0")
        else:
            print("$20")
    else:
        print("$100")

main()