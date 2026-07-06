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

#Making table using For Loop

for i in range(1,20,1):
	print("5*",i,"=",5*i)

#if loop

a = 21

if a == 21:
	print("The value of a is 21")
elif a > 21:
	print("The value of a is Greater than 21")
else : 
	print("The value of a is Less than 21")

#Marks Grade Code (Incompelete)

print("Please Input your Marks below respective to given Subjects!")

Mathematics = float(input("Enter your Marks for Mathematics:"))
Science = float(input("Enter your Marks for Science:"))
English = float(input("Enter your Marks for English:"))
Python = float(input("Enter your Marks for Python:"))
DSA = float(input("Enter your Marks for DSA:"))

Marks = [Mathematics,Science,English,Python,DSA]
Subjects = ['Mathematics','Science','English','Python','DSA']

for i in range Marks:
 for j in range Subjects:
  if i >= 93:
   print ("Your Grade in",Subjects[j],"Subject is AA")
  elif 70<=i and i<=92:
   print ("Your Grade in",Subjects[j],"Subject is BB")
  elif 60<=i and i<=69:
   print ("Your Grade in",Subjects[j],"Subject is CC")
  elif 50<=i and i<=59:
   print ("Your Grade in",Subjects[j],"Subject is DD")
  elif 19<=i and i<=49:
   print ("Your Grade in",Subjects[j],"Subject is EE")
  elif 0<=i and i<=18 :
   print ("Sorry Better Luck Next This Time Hahahha")
  else :
   print ("Please Provide Valid Marks")

