#Marks Code Basic Logic Version 1

# print("Please Input your Marks below respective to given Subjects!")

# M1 = float(input("Enter your Marks for Mathematics:"))
# M2 = float(input("Enter your Marks for Science:"))
# M3 = float(input("Enter your Marks for English:"))
# M4 = float(input("Enter your Marks for Python:"))
# M5 = float(input("Enter your Marks for DSA:"))

# Total = M1+M2+M3+M4+M5
# if Total>=0 and Total<=100:
#     print ("Your total marks are:",Total)

# if Total >= 93 and Total<=100:
#     print ("Your Grade is AA")
# elif 70<=Total and Total<=92:
#     print ("Your Grade is BB")
# elif 60<=Total and Total<=69:
#     print ("Your Grade is CC")
# elif 50<=Total and Total<=59:
#     print ("Your Grade is DD")
# elif 19<=Total and Total<=49:
#     print ("Your Grade is EE")
# elif 0<=Total and Total<=18 :
#     print ("Sorry Better Luck Next This Time Hahahha FAILED")
# else :
#     print ("Please Provide Valid Marks")



#Marks Code Basic Logic Version 2

print("Please Input your Marks below respective to given Subjects!")

M1 = float(input("Enter your Marks for Mathematics:"))
M2 = float(input("Enter your Marks for Science:"))
M3 = float(input("Enter your Marks for English:"))
M4 = float(input("Enter your Marks for Python:"))
M5 = float(input("Enter your Marks for DSA:"))

Marks = [M1,M2,M3,M4,M5]
Subjects = dict(Mathematics = M1, Science = M2, English = M3, Python = M4, DSA = M5)

Total = M1+M2+M3+M4+M5/5
if Total>=0 and Total<=100:
    print ("Your total marks are:",Total)

for x in Subjects:
    if Subjects[x]>=0 and Subjects[x]<=17:
        print("You are Failed in Subject:",x)
    else:
        if Subjects[x]>=92 and Subjects[x]<=100:
            print("Your Grade in Subject",x,"is A+")
        elif Subjects[x]>=80 and Subjects[x]<=91:
            print("Your Grade in Subject",x,"is A")
        elif Subjects[x]>=54 and Subjects[x]<=79:
            print("Your Grade in Subject",x,"is B+")
        elif Subjects[x]>=35 and Subjects[x]<=53:
            print("Your Grade in Subject",x,"is A")
        elif Subjects[x]>=18 and Subjects[x]<=34:
            print("Your Grade in Subject",x,"is C")                     

if Total >= 417 and Total<=500:
    print ("Your Grade is A")
else :
    if Total >= 0 and Total<=416:     
        if 300<=Total and Total<=416:
            print ("Your Grade is B")
        elif 200<=Total and Total<=299:
            print ("Your Grade is C")
        elif 100<=Total and Total<=199:
            print ("Your Grade is D")
        elif 0<=Total and Total<=99:
            print ("Your Grade is E")
        elif Total<0 and Total>500:
            print ("Enter Valid Marks")    
    else :
        print ("Sorry Better Luck Next This Time Hahahha")


        
