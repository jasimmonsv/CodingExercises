#! /usr/bin/python

answerx = 0
answery=0
    
def palindrom(num):
    palin=''
    tmp = str(num)
    y=0
    for x in reversed(range(len(tmp))):
        palin=palin+str(tmp[x])
        y=y+1
    return int(palin)
    
for x in range(100,999):
    for y in range(100,999):
        if (x * y) == palindrom(x*y):
            if x*y > answerx*answery:
                answerx = x
                answery = y 
        y=y+1
    y=100
    x = x+1

print(answerx)
print(answery)  
print(answerx * answery)          