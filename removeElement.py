"""
Remove an Element from a List
=============================

@author: mhtehrani
October 28, 2021
https://github.com/mhtehrani

"""

def removeElement(nums, val):
    left = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[left], nums[j] = nums[j], nums[left]    
            left += 1
        #end
    #end
    
    return left
#end

print(removeElement([0,1,2,2,3,0,4,2],2))