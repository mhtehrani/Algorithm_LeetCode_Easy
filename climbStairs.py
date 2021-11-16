"""
All the Possible Stair Climbing
===============================

@author: mhtehrani
October 31, 2021
https://github.com/mhtehrani

"""

def climbStairs(n):
    step = [0]*max(3,n+1)
    step[0] = 0
    step[1] = 1
    step[2] = 2
    for i in range(3,n+1):
        step[i] = step[i-1]+step[i-2]
    #end
    return step[n]

print(climbStairs(5))