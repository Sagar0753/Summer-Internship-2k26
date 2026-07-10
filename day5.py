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

# Take a number and check whether it is zero, positive or negative using nested IF…ELSE statement.
num = float(input("Enter any Number:"))
if num == 0:
    print("Entered Number is zero")
elif num>0:
    print("Entered Number is Postive")
else:
    print("Entered Number is Negative")

# Take 3 numbers and find greatest number using nested IF….ELSE statement.
n1 = float(input("Enter Number 1:"))
n2 = float(input("Enter Number 2:"))
n3 = float(input("Enter Number 3:"))
if n1>=n2: 
    if n1>=n3:
        print("Number 1 is greatest")
elif n2>=n1: 
    if n2>=n3:
        print("Number 2 is greatest")
else:
    print("Number 3 is greatest")

# Take 3 numbers and find smallest number using logical operator
n1 = float(input("Enter Number 1:"))
n2 = float(input("Enter Number 2:"))
n3 = float(input("Enter Number 3:"))
if n1<=n2 and n1<=n3:
    print("Number 1 is smallest")
elif n2<=n1 and n2<=n3:
    print("Number 2 is smallest")
else:
    print("Number 3 is smallest")

# Take a number and find factorial of that number.
num = int(input("Enter any Number:"))
temp = 1
if num == 0 or num == 1:
    print("The Factorial of a given number is: 1")
for i in range(num):
    if num>1:
        temp = temp * num
        num = num - 1
print("The Factorial of a given number is:",temp)

# Write a program to swap 2 numbers using third variable.
a = 10
b = 20
temp
print("Before Swapping the elements are: a =",a,"b =",b)
temp = a
a = b
b = temp
print("After Swapping the elements are: a =",a,"b =",b)

# Take a number. Generate multiplication table of that number.
num = int(input("Enter any Number:"))
mul = int(input("Enter the number of multiplicative terms:"))
print("The Multiplication table of",num,"is shown below")
for x in range(mul):
    print("5 x",x+1,"=",5*(x+1))

# Take a number and calculate sum of natural numbers.
num = int(input("Enter any Number:"))
temp = 0
while num != 0:
    temp += num
    num -= 1
print("The Sum of Natural number till the given number is:",temp)

# Take a number. If number is 1 then print Monday, 2 then print Tuesday and so on…
num = int(input("Enter any Number between 1 to 7:"))
if num >= 1 and num <= 7:
    if num == 1:
        print("Today is Monday!")
    elif num == 2:
        print("Today is Tuesday!")
    elif num == 3:
        print("Today is Wednesday!")
    elif num == 4:
        print("Today is Thursday!")
    elif num == 5:
        print("Today is Friday!")
    elif num == 6:
        print("Today is Saturday!")
    elif num == 7:
        print("Today is Sunday!")
else:
    print("Please Enter a number between 1 to 7 only!")

# Take a number between 1 to 12.If number is 1 then print January, 2 then print February and so on… (Use match case)
num = int(input("Enter any Number between 1 to 12:"))
if num >= 1 and num <= 12:   
    match num:
      case 1:
        print("January")
      case 2:
        print("February")
      case 3:
        print("March")
      case 4:
        print("April")
      case 5:
        print("May")
      case 6:
        print("June")
      case 7:
        print("July")
      case 8:
        print("August")
      case 9:
        print("September")
      case 10:
        print("October")
      case 11:
        print("November")
      case 12:
        print("December")
else:
    print("Please Enter a number between 1 to 12 only!")
