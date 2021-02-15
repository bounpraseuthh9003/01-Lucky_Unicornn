# Ask the user if they have played before
played_before = input("Have you played this game before? ").lower()

# If they say yes, output 'program continues'
# If they say no, output 'display instructions'
# If the answer is invalid, print an error.
if played_before == "yes":
    print("program continues")

elif played_before == "y":
    print("program continues")

elif played_before == "no":
    print("display instructions")

elif played_before == "n":
    print("display instructions")

else:
    print("Please answer yes / no")
