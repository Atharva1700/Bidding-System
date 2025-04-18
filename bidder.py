def highest_bidder(bid_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bid_dictionary:
        bid_amount = bid_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"{winner} is the winner with a bid of ${highest_bid}")

bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name? ")
    price = float(input("What is your bid?: $"))
    bids[name] = price
    continu = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if continu == "no":
        continue_bidding = False
        highest_bidder(bids)
    elif continu == "yes":
        print("\n" * 10)
