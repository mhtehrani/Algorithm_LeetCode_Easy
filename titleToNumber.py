"""
Generate the Corresponding Excel Sheet Column Number
====================================================

@author: mhtehrani
November 08, 2021
https://github.com/mhtehrani

"""

def titleToNumber(columnTitle):
    dic = {"Z": 0, "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9,
           "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
           "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25}
    
    remainder = []
    for a in columnTitle:
        remainder.append(dic[a])
    #end
    
    Quotient = 0
    for i in range(len(remainder)):
        if remainder[i] == 0:
            Quotient += 1
        #end
        Quotient = 26*Quotient+remainder[i]
    #end
    
    return Quotient
#end

print(titleToNumber("ZY"))