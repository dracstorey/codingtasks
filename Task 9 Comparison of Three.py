number1 = int(input("Input a number"))
number2 = int(input("Input a second number"))
number3 = int(input("Input a third number"))
if number1 > number2 and number1> number3 and number2 > number3:
    print (number1, number2, number3)
elif number1 > number2 and number1> number3 and number3 > number2:
    print (number1, number3, number2)
elif number2 > number1 and number2> number3 and number3 > number1:
    print (number2, number3, number1)
elif number2 > number1 and number2> number3 and number1 > number3:
    print (number2, number1, number3)
elif number3 > number1 and number3> number1 and number2 > number1:
    print (number3, number2, number1)
elif number3 > number1 and number3> number1 and number1 > number2:
    print (number3, number1, number2)