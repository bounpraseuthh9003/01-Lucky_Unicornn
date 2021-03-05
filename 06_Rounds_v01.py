# set balance for testing purposes
balance = 5

rounds_played = 0

to_play = input("Press <Enter> to play... ").lower()
while to_play == "":

    # increase number of  rounds played
    rounds_played += 1

    # print round number
    print()
    print("*** Round #{} ***".format(rounds_played))
    balance -= 1
    print("Balance: ", balance)
    print()

    if balance < 1:
        to_play = "xxx"
        print("Sorry, you have run out of money")
    else:
        to_play = input("Press <Enter> to play or 'xxx' to quit ")

print()
print("Final Balance: ", balance)
