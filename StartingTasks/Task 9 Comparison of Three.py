## Task 9 - input 3 numbers then output in order

# User inputs 3 nunbers
a = int(input("Input a number"))
b = int(input("Input a second number"))
c = int(input("Input a third number"))

# check a and b and swap if a is larger
if a > b:
    # swap a and b over
    temp = a
    a = b
    b = temp

# Check a against c and swap if larger
if a > c:
    # swap a and c over
    temp = a
    a = c
    c = temp

# smallest is now in posiiton a so check b against c
if b > c:
    # swap ba nd c over
    temp = b
    b = c
    c = temp

 ## Print in order   
print (a, "<", b, "<", c)
