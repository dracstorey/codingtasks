## Task 3 - ask for an option number betwene 1 and 3. 


#get user to choose a number (1-3) and convert to integer
number = int(input("Choose 1,2 or 3"))

# check if number is between 1 and 3
while number < 1 or number > 3:
    
    # Ask for the number again
    number = int(input("Choose 1,2 or 3"))
    
#endwhile

# Print correct output
print("You have selected option number", number)




    
   
