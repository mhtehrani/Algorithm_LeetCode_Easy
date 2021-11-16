"""
Add Two Binary Numbers
======================

@author: mhtehrani
October 31, 2021
https://github.com/mhtehrani

"""

def binaryToNum(a):
    num = 0
    for i in a:
        num = num*2 + int(i)
    #end
    return num
#end

def numToBinary(a):
    quotient = a // 2
    remainder = str(a % 2)
    a = quotient
    while quotient > 0:
        quotient = a // 2
        remainder += str(a % 2)
        a = quotient
    #end
    return remainder[::-1]
#end

def addBinary(a, b):
    object = numToBinary(binaryToNum(a) + binaryToNum(b))
    return object
#end

print(addBinary('11', '1'))