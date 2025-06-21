print("Welcome to the secret auction program.")

auction_dict = {}

while True:
    name = input("What is your name? ")
    bid = int(input("Whar's your bid? $"))
    auction_dict[name] = bid

    question = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if question == 'yes':
        print("\n" * 200)
    else:
        print("\n" * 200)
        break

highest_bidder = ""
highest_bid = 0

for key in auction_dict:
    if auction_dict[key] > highest_bid:
        highest_bid = auction_dict[key]
        highest_bidder = key

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")