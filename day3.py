#Taking 5 numbers as input from user and calculating the maximum and sorting it in a ascending order without list

Numbers = ['','','','','']
sorted = ['','','','','']

for i in range(len(Numbers)):
    print("Enter number ",i,":",)
    x = int(input())
    Numbers[i] = x

print(Numbers)

Max = 0

for i in range(0,5):
    if Numbers[i] >= Max:
        Max = Numbers[i]

for i in range(0,5):
    if Max == Numbers[i]:
        Numbers[i] = 0
        
print("Maximum Number:", Max)
