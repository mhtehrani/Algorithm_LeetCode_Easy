"""
Find the Only Single Number
===========================

@author: mhtehrani
November 05, 2021
https://github.com/mhtehrani

"""

def singleNumber(nums):
    dic = {}
    for i in nums:
        if i in dic:
            dic.pop(i)
        else:
            dic[i] = i
        #end
    #end
    num = dic.popitem()
    return num[0]
#end

print(singleNumber([2,2,1]))
            