"""
Finding the Index of a Target Value in a List
=============================================

@author: mhtehrani
October 28, 2021
https://github.com/mhtehrani

"""

def searchInsert(nums, target):
    left = 0
    right = len(nums)-1
    
    while right >= left:
        mid = (left+right)//2
        
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            if left <= mid-1:
                right = mid-1
            else:
                return left
            #end
        elif nums[mid] < target:
            if mid+1 <= right:
                left = mid+1
            elif mid == right:
                return right+1
            else:
                return right
            #end
        #end
    #end
#end

print(searchInsert([1], 2))