
## Task 5 - Input a 3 digit number and output hundreds, tens and units

# Input number form user (no vliadation chekc!)
number = int(input("Input an integer between 100 and 999"))

## Calculate hundereds
hundreds = number//100

# Calcuate tens (number substract hundreds * 100)
tens = (number - (number//100)*100)//10

# Calculate units (number subtract hundereds * 100 and 10 * tens)
units =(number - (number//100)*100) - ((number - (number//100)*100)//10)*10

## Output result
print (hundreds, " hundreds", tens, " tens", units, " units" )

