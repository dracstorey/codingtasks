f = open('input.txt','r')
data = f.read()
f.close()
print(data)

v = data.split(",")
for c in v:
    t = c.split(":")
    print (t[0],t[1])

##f = open('input.txt','r',newline='')
##for line in f:
##    print(line)
##f.close()

##data = 'Test 1\n' \
##       'Test 2' + chr(10) + \
##       'Test 3\n' \
##       'Test 4\n'
##
##f = open('output1.txt', 'w')
##f.write(data)
##f.close()
##
##f = open("output2.txt", 'w')
##print(data, file=f)
##f.close()