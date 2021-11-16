"""
Remove Duplicates
=================

@author: mhtehrani
October 27, 2021
https://github.com/mhtehrani

"""

def removeDuplicates(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[i] < nums[j]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
        #end
    #end
    
    return i+1
#end

print(removeDuplicates([1,1,2]))
            