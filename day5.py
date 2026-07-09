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
