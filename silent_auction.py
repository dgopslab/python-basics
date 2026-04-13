def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            winner = bidder
            highest_bid = bid_amount

    if winner:
        print(f"The winner is {winner} with a bid of €{highest_bid}.")
    else:
        print("No bids were placed.")


bids = {}
more_bidders = True

while more_bidders:
    name = input("What is your name? ")
    bid = int(input("What is your bid? €"))
    bids[name] = bid

    more = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if more == "no":
        more_bidders = False
        find_highest_bidder(bids)
    elif more == "yes":
        print("\n" * 100)
    else:
        print("Input not recognized. Showing current result.")
        more_bidders = False
        find_highest_bidder(bids)
