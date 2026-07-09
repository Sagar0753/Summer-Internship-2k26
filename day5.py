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

