#TAsk 11: Input hrs, mins and seconds and convert to secondws

# Get user input in the format hh:mm:ss
x = input("time (hh:mm:ss)  ")

#Use the split function to create a list of three elements
time_list = x.split(":")

#Claculate seconds time_list[0] times 3600 and add time_list[1] times 60 etc
# Note each element is a string and so needs converting to integer
seconds = int(time_list[0])*3600+int(time_list[1])*60 + int(time_list[2])

# Print out the number of seconds
print (seconds, "seconds")