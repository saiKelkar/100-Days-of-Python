letters_dict = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j", 11: "k", 12: "l", 13: "m", 14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s", 20: "t", 21: "u", 22: "v", 23: "w", 24: "x", 25: "y", 26: "z"}

command = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
message = input("Type your message: ")
number_shift = int(input("Type the shift numbers: "))


if command == 'encode':
    for i in message:
        if i in letters_dict.values():
            letters_key = list(letters_dict.keys())[list(letters_dict.values()).index(i)]
            new_key = (letters_key + number_shift)

        print(letters_dict[new_key], end ="")
    
elif command == 'decode':
    for i in message:
        if i in letters_dict.values():
            letters_key = list(letters_dict.keys())[list(letters_dict.values()).index(i)]
            new_key = (letters_key - number_shift)

        print(letters_dict[new_key], end="") 