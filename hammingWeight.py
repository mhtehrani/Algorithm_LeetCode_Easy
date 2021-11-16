"""
Number of '1' Bits (Hamming Weight)
===================================

@author: mhtehrani
November 10, 2021
https://github.com/mhtehrani

"""

def hammingWeight(n):
    Quotient = n
    sum_ = 0
    for i in range(32):
        sum_ += (Quotient % 2)
        Quotient = Quotient//2
    #end
    
    return sum_
#end

print(hammingWeight(11))