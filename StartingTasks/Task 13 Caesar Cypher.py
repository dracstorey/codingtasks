##Task 13 - Implement a Caesar Cypher

#Get input from the user
message = "HELLO HOW ARE YOU"

#Set the shift value
shift_value = 3

new_word = ""

#print (chr((ord("B")-64 + shift_value)%26 + 64))


# Initialse the counter
counter = 0


# Lloop round each letter of the message
while counter < len(message):
    # Deal with spaces
    if message[counter] == " ":
        new_word = new_word + " "
    else:
        # get ascii value, substract 65 (value of A) add shift value, find module 26 (l;etters in alphabte) and add 65 on.
        new_word = new_word +  (chr((ord(message[counter])-65 + shift_value)%26 + 65))
    #end if
    # Increment the counter
    counter = counter + 1

#Print out the new messgae
print (new_word)

    