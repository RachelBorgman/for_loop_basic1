for x in range(151):
    print(x)

for x in range(5,1000,5):
    print(x)

for i in range(1,100):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

sum = 0
for i in range(1,500000,2):
    sum = sum + i
print(sum)

x = 2018
while x > 0:
    print(x)
    x -=4

lowNum = 2
highNum = 9
mult = 3
while lowNum < highNum+1:
    if lowNum % mult == 0:
        print(lowNum)
    lowNum +=1
