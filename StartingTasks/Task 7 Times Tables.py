## User inputs a number and the first 12 of the times table is outputted

# Initialise counter
counter = 1

# Get number form the user (no validation!)
number = int(input("Input a number between 1-10"))

# Loop round 10 times
while counter < 11:
    
    # Print the value times counter
    print(counter, "times", number, " = ", number*counter)

    # increment counter
    counter = counter + 1 

#endwhile

