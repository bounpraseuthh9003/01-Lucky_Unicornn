played_before = ""
while played_before.lower() != "xxx":
    # Ask the user if they have played before
    played_before = input("Have you played this game before? ").lower()

    # If they say yes, output 'program continues'
    # If they say no, output 'display instructions'
    # If the answer is invalid, print an error.
    if played_before == "yes" or played_before == "y":
        played_before = "yes"
        print("program continues")

    elif played_before == "no" or played_before == "n":
        played_before = "no"
        print("display instructions")

    else:
        print("Please answer yes / no")

    print("You chose {}".format(played_before))
