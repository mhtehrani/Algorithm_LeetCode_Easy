"""
Reverse Bits of a Given 32 Bits Unsigned Integer
================================================

@author: mhtehrani
November 10, 2021
https://github.com/mhtehrani

"""

def reverseBits(n):
    Quotient = n
    QuotientNew = 0
    for i in range(32):
        QuotientNew = QuotientNew*2 + (Quotient % 2)
        Quotient = Quotient//2
    #end
    
    return QuotientNew
#end

print(reverseBits(43261596))