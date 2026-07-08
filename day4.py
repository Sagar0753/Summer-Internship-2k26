#Calculate area of a rectangle.(Formula :- L*B)

Length = float(input("Enter the length of 4-side polynomial:"))
Breadth = float (input("Enter the breadth of 4-side polynomial:"))

Area = Length * Breadth

if Length == Breadth:
    print("The the Area of Sqaure is:",Area)
else:
    print("The the Area of rectangle is:",Area)