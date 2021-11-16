"""
Convert Roman Number to Integer
===============================

@author: mhtehrani
October 27, 2021
https://github.com/mhtehrani

"""

number = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

roman = "IX"

roman = roman[::-1]
num_pre = number[roman[0]]
sum = num_pre

for i in range(1,len(roman)):
    num_cur = number[roman[i]]
    
    if num_cur >= num_pre:
        sum += num_cur
    else:
        sum -= num_cur
    #end
    
    num_pre = num_cur
#end

print(sum)    