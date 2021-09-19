## Print out the factors of a number



# Get the user input and covert to integer
number = int(input("Input an integer"))

counter = 1
# Print first part of the statement
print("The factors of ", number, "are: ")

# Loop round all number between 1 and half of the given number
while counter < number // 2 + 1:
    
    # Check if it divides .. remainder will be zero
    if number%counter == 0:
        # Print the divisor
        print(counter)
    #endif
   
   # increase the counter
    counter = counter + 1
#endwhile
