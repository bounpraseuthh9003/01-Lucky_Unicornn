

# Function goes here...
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")


# Main Routine goes here...
played_before = yes_no("Have you played this game before? ")
print("You chose {}".format(played_before))
print()
having_fun = yes_no("Are you having fun? ")
print("You chose {} to having fun".format(having_fun))
