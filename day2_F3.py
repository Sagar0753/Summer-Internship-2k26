#Marks Code Basic Logic Version 1

print("Please Input your Marks below respective to given Subjects!")

M1 = float(input("Enter your Marks for Mathematics:"))
M2 = float(input("Enter your Marks for Science:"))
M3 = float(input("Enter your Marks for English:"))
M4 = float(input("Enter your Marks for Python:"))
M5 = float(input("Enter your Marks for DSA:"))

Total = M1+M2+M3+M4+M5
if Total>=0 and Total<=100:
    print ("Your total marks are:",Total)

if Total >= 93 and Total<=100:
    print ("Your Grade is AA")
elif 70<=Total and Total<=92:
    print ("Your Grade is BB")
elif 60<=Total and Total<=69:
    print ("Your Grade is CC")
elif 50<=Total and Total<=59:
    print ("Your Grade is DD")
elif 19<=Total and Total<=49:
    print ("Your Grade is EE")
elif 0<=Total and Total<=18 :
    print ("Sorry Better Luck Next This Time Hahahha FAILED")
else :
    print ("Please Provide Valid Marks")
