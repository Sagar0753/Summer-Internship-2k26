#Calculate area of a rectangle.(Formula :- L*B)

Length = float(input("Enter the length of 4-side polynomial:"))
Breadth = float (input("Enter the breadth of 4-side polynomial:"))

Area = Length * Breadth

if Length == Breadth:
    print("The the Area of Sqaure is:",Area)
else:
    print("The the Area of rectangle is:",Area)

#Calculate area of a rectangle.

Length = float(input("Enter the length of rectangle:"))
Breadth = float (input("Enter the breadth of rectangle:"))
Area = Length * Breadth

print("The the Area of rectangle is:",Area)

#Calculate area of a circle.(Formula :- pi*r*r)

pi = 3.14
r = float(input("Enter the radius of Circle: "))
d = 2 * r
area = pi * r * r
print("Are of Circle is:",area)
print("Are of Diameter is:",d)
