"""
Majority Element (Greater Than n/2)
===================================

@author: mhtehrani
November 08, 2021
https://github.com/mhtehrani

"""

def majorityElement(nums):
    dic = {}
    for n in nums:
        if n in dic:
            dic[n] += 1
        else:
            dic[n] = 1
        #end
    #end
    
    maj_n = nums[0]
    maj = 0
    for n in dic:
        if dic[n] > maj:
            maj_n = n
            maj = dic[n]
        #end
    #end
    
    return maj_n
#end

print(majorityElement([2,2,1,1,1,2,2]))