# Write a program to enter the temperature in Fahrenheit and convert it to Celsius.
F = float(input("Enter the Temperature in Fahrenheit:"))
C = ((F-32)*5)/9 
print("Temperature in Celsius is:",C)

# Check whether number is even or odd.
num = int(input("Enter any Number:"))
if num % 2 == 0:
    print("Entered Number is even")
else:
    print("Entered Number is odd")

# Take a year and check whether it is leap year or not.
year = int(input("Enter any Year"))
if year % 4 == 0:
    print("Its a Leap Year")
else:
    print("Not a Leap year")

# Write a program to enter two numbers and find the smallest out of them using conditional operator.
n1 = float(input("Enter Number 1:"))
n2 = float(input("Enter Number 2:"))
if n1<=n2:
    print("Number 1 is smallest number.")
else:
    print("Number 2 is smallest number.")

# Take a number and check whether it is zero, positive or negative.
num = float(input("Enter any Number:"))
if num == 0:
    print("Entered Number is zero")
elif num>0:
    print("Entered Number is Postive")
else:
    print("Entered Number is Negative")

# Take 2 numbers and display greatest number. (Number can be equal).
n1 = float(input("Enter Number 1:"))
n2 = float(input("Enter Number 2:"))
if n1>=n2:
    print("Number 1 is greatest number.")
else:
    print("Number 2 is greatest number.")

# Take age and whether it is less than 18 or not. If it is less than 18 then print not eligible for vote.
age = int(input("Enter you age:"))
if age >= 18:
    print("You are eligible to Vote")
else:
    print("Your are not eligible to Vote")

# Write a program to check whether the blood donor is eligible or not for donating blood. The conditions is Age should be above 18 year but not more than 55 year.
age = int(input("Enter you age:"))
if age >= 18 & age <= 55:
    print("You are eligible to Donate Blood")
else:
    print("Your are not eligible to Donate Blood")

# Take 2 numbers and find smallest number.
n1 = float(input("Enter Number 1:"))
n2 = float(input("Enter Number 2:"))
if n1<=n2:
    print("Number 1 is smallest number.")
else:
    print("Number 2 is smallest number.")

# Take a number check if a number is less than 100 or not. If it is less than 100 then check if it is odd or even.
n = float(input("Enter Number:"))
if n > 100:
    print ("Entered Number is greater than 100")
elif n == 100:
    print("Entered Number is 100")
else:
    if n%2 == 0:
        print("Entered Number is less than 100 and an even number")
    else:
        print("Entered Number is less than 100 and an odd number")

# Take a number to print the square of a number if it is less than 10.
n = float(input("Enter Number:"))
if n<10:
    sq = n*n
    print("The given number is less than 10 and its square is:",sq)
else:
    print("The given number is greater than or equal to 10")
