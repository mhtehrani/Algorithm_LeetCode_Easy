"""
Add One to a List of an Integer
===============================

@author: mhtehrani
October 31, 2021
https://github.com/mhtehrani

"""

def plusOne(digits):
    digits[len(digits)-1] += 1
    for i in range(len(digits)-1,0,-1):
        if digits[i] == 10:
            digits[i] = 0
            digits[i-1] += 1
        #end
    #end
    if digits[0] == 10:
        aa = [1,0]
        aa.extend(digits[1:len(digits)])
        return aa
    #end
    return digits

print(plusOne([9,9,9]))