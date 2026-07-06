#Printing in Same line 
print("Hello World,", end=" ")
print("My name is Sagar!")

#Printing Numbers
print(359012)
print(100)

#Printing Numbers doesnt require Commas
print (10+20)
print (10-20)

a = 10
b = 20
c = a + b
print ("Add of A + B is",c,"as Output")

'''Taking as Input from User
as float and printing as integer and both float'''

x = float(input("Enter Value of x:"))
y = float(input("Enter Value of y:"))
z = x + y
print ("The output of Operation on given numbers in interger value is:",int(z))
print ("The output of Operation on given numbers in float value is:",float(z))

#We can also Type Cast x and y directly in z

p =  input("Enter the Value 1:")
q =  input("Enter the Value 2:")
r =  float(p) + float(q)
print ("The Output of r in float value will be:",r)

#By default if we dont give any Data Type to the input taken from User than it will be taken as String only

p =  input("Enter the Value 1:")
q =  input("Enter the Value 2:")
r =  p + q
print ("The Output without Type casting will be",r)

