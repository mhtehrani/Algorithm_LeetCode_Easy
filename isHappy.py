"""
Happy Number
============

@author: mhtehrani
November 10, 2021
https://github.com/mhtehrani

"""

def isHappy(n):
    dic = {n:n}
    while True:
        sum_ = 0
        for i in range(len(str(n))):
            sum_ += (n % 10)**2
            n = n//10
        #end
        n = sum_
        if n == 1:
            return True
        elif n in dic:
            return False
        else:
            dic[n] = n
        #end
    #end
    
    return False
#end

print(isHappy(19))