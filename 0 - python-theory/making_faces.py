def main():
    greeting = input()
    emoticon(greeting)

def emoticon(greeting):
    greeting = greeting.replace(":)", "🙂").replace(":(", "🙁")
    print(greeting)

main()