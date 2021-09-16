##Task 14 - Reverse a given string

# User input
myString = input("Input a string")

# Initialiuse Output string
reverseString = ""

# Initialise counter
counter = len(myString) - 1

# Loop round from end of string to finrt (index = 0)
while counter >= 0:

    # concatenate output string with curretn character
    reverseString = reverseString + myString[counter]

    # decrease counter
    counter = counter - 1
# endwhile

# Print output
print ("Reverse string is:", reverseString)
