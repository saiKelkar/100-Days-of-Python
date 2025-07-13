def main():
    speech = input()
    string_edit(speech)

def string_edit(speech):
    print(speech.replace(" ", "..."))

main()