#Write a program to enter the temperature in Fahrenheit and convert it to Celsius.
F = float(input("Enter the Temperature in Fahrenheit:"))
C = ((F-32)*5)/9 
print("Temperature in Celsius is:",C)

#Check whether number is even or odd.
num = int(input("Enter any Number:"))
if num % 2 == 0:
    print("Entered Number is even")
else:
    print("Entered Number is odd")

#Take a year and check whether it is leap year or not.
year = int(input("Enter any Year"))
if year % 4 == 0:
    print("Its a Leap Year")
else:
    print("Not a Leap year")
