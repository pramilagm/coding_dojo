# Basic - Print all integers from 0 to 150.
for i in range(0,151):
    print(i)

# Multiples of Five - Print all the multiples of 5 from 5 to 1,00
for i in range(5,101):
    print(i*5)

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for i in range(0,500000):
    sum += i
print(sum)

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for i in range(2018,0,-4):
    print(i)

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the
#  integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum =2
highNum = 9
mult = 3
for i in range(lowNum,highNum+1):
    if i%mult==0:
        print(i)

