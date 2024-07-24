low = 1
high = 1000

print("Please think of a number between {0} and {1}".format(low, high))
print("Press enter to start")

numGuesses = 0

while low != high:
    print("Guessing in the range of {0} to {1}".format(low, high))

    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower?"
                     " Enter h, l or c if I'm correct ".format(guess)).casefold()
    numGuesses += 1
    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print("I guessed correctly in {} guesses".format(numGuesses))
        break
    else:
        print("Invalid input. Please enter h for higher, l for lower, or c if correct ")
else:
    print("You thought of the number {}".format(low))
    print("It took me {} guesses".format(numGuesses))
