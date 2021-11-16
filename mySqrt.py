"""
Closest Square Root
===================

@author: mhtehrani
October 31, 2021
https://github.com/mhtehrani

"""

def mySqrt(x):
    UB = int(x)
    LB = 0
    if x == 1:
        return 1
    while True:
        guess = (UB + LB) // 2
        if guess*guess == x:
            return guess
        elif guess*guess > x:
            UB = guess + 1
        elif guess*guess < x and (guess+1)*(guess+1) > x:
            return guess
        else:
            LB = guess
        #end
    #end
#end

print(mySqrt(17))