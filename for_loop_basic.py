# print all int from 0 to 150
for x in range(0,151,1):
    print(x)

# print all the multiples of 5 from 5 to 1000
for x in range(0,1000,5):
    print(x)

# print int 1 to 100. if divisible by 5, print "coding" instead. if divisible by 10, print "coding dojo"
for x in range(0,101,1):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)


# Add odd ints from 0 to 500,000 and print the final sum
mySum = 0

for x in range(0,500000,1):
    if x & 1 == 1:
        mySum += x

print(mySum)


# Print positive numbers starting at 2018, counting down by fours
for x in range(2018,0,-4):
    print(x)

#  Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 28
mult = 4

for x in range(lowNum,highNum+1,1):
    if x % mult == 0:
        print(x)
