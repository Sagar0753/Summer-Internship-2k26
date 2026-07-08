#1.Calculate area of a rectangle.(Formula :- L*B)

Length = float(input("Enter the length of 4-side polynomial:"))
Breadth = float (input("Enter the breadth of 4-side polynomial:"))

Area = Length * Breadth

if Length == Breadth:
    print("The the Area of Sqaure is:",Area)
else:
    print("The the Area of rectangle is:",Area)

#2.Calculate area of a rectangle.

Length = float(input("Enter the length of rectangle:"))
Breadth = float (input("Enter the breadth of rectangle:"))
Area = Length * Breadth

print("The the Area of rectangle is:",Area)

#3.Calculate area of a circle.(Formula :- pi*r*r)

pi = 3.14
r = float(input("Enter the radius of Circle: "))
d = 2 * r
area = pi * r * r
print("Are of Circle is:",area)
print("Are of Diameter is:",d)

#4.Calculate average of n numbers.

Numbers = []
Count = int(input("Enter How many Numbers :"))
total = 0

for i in range(Count):
    print("Enter number",i + 1,":")
    var = float(input())
    Numbers.append(var)
    total += var

print("All the Given numbers are",Numbers)
print("The total of all the numbers is:",total)
avg = total/int(Count)
print ("The Average of the 5 numbers is:",avg)

#5.Calculate Simple interest.(Formula :- (p*r*t)/100)

p = float(input("Enter the Principal:"))
r = float(input("Enter the Annual interest rate:"))
t = float(input('Enter the time in years:'))
sim = p*r*t
interest = sim/100
print ("The Simple Interest on the Amount for",t,"Year will be",interest,"Rupees")
