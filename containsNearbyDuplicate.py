"""
Contains Nearby Duplicate
=========================

@author: mhtehrani
November 11, 2021
https://github.com/mhtehrani

"""

# def containsNearbyDuplicate(nums,k):
#     for i in range(len(nums)-1):
#         if nums[i] in nums[i+1:min(i+k+1,len(nums))]:
#             return True
#         #end
#     #end
    
#     return False


            
def containsNearbyDuplicate(nums, k):
    d={}
    for i in range(len(nums)):
        if nums[i] not in d or abs(i-d[nums[i]])>k :
            d[nums[i]]=i
        else:
            return True

print(containsNearbyDuplicate([1,2,3,4,5,6,7,8,1],3))