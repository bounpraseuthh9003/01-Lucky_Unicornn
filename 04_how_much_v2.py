# Functions go here...
def number_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low / too high give
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine goes here...
for item in range(0, 10+1):
    how_much = number_check("How much would you like to play with? ", 0, 10)
    print("You will be spending ${}".format(how_much))
