#Taking num1 as input from User
num1=int(input("Enter number 1="))
print(f"First number entered is {num1}")
#Taking num2 as input from User
num2=int(input("Enter number 2="))
print(f"Second number entered is {num1}")
#Finding minimum of two numbers
if(num1<num2) :
    print(f"Number 1 is minimum and number entered is {num1}")
    #comaring two numbers in case of both entered numbers are same
elif(num1==num2):
    print(f"Both the numbers are equal and number entered is {num2}")
    #Printing in case of number 2 is minimum
else:
    print(f"Number 2 is minimum and number entered is {num2}")