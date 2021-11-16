"""
Generate the Excel Sheet Column Title Like
==========================================

@author: mhtehrani
November 08, 2021
https://github.com/mhtehrani

"""

def convertToTitle(columnNumber):
    dic = {0:"Z", 1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I",
           10: "J", 11: "K", 12: "L", 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q",
           18: "R", 19: "S", 20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y"}
    
    remainder = [columnNumber % 26]
    if remainder[len(remainder)-1] == 0:
        Quotient = (columnNumber // 26) -1
    else:
        Quotient = columnNumber // 26
    #end
    while Quotient != 0:
        remainder.append(Quotient % 26)
        if remainder[len(remainder)-1] == 0:
            Quotient = (Quotient // 26) -1
        else:
            Quotient = Quotient // 26
        #end
        
    #end
    
    name = ""
    for i in remainder[::-1]:
        name += dic[i]
    #end
    
    return name
#end

print(convertToTitle(2147483647))