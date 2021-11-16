"""
Contains Duplicate
==================

@author: mhtehrani
November 11, 2021
https://github.com/mhtehrani

"""

def containsDuplicate(nums):
    dic = {}
    
    for i in nums:
        if i in dic:
            return True
        else:
            dic[i] = i
        #end
    #end
    
    return False

print(containsDuplicate([1,2,3,1]))
            

