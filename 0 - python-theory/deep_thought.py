def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    user_answer(answer)

def user_answer(answer):
    if answer == "42" or answer == "forty-two" or answer == "forty two":
        print("Yes")
    else:
        print("No")

main()