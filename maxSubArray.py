"""
Maximum Subarray
================

@author: mhtehrani
October 28, 2021
https://github.com/mhtehrani

"""

def maxSubArray2(nums):
    best_val = nums[0]
    best_list = nums[0:1]
    current_val = nums[0]
    current_list = nums[0:1]
    L = 0
    
    for i in range(1,len(nums)):
        if current_val <= nums[i] and current_val <= 0:
            current_val = nums[i]
            current_list = nums[i:i+1]
            L = i
            if current_val > best_val:
                best_val = current_val
                best_list = current_list
            #end
        elif nums[i] > 0:      # if number_i is positive
            current_val += nums[i]
            current_list = nums[L:i+1]
            if current_val > best_val:
                best_val = current_val
                best_list = current_list
            #end
        else:                                   # if number_i is negative
            if current_val > 0:
                current_val += nums[i]
                current_list = nums[L:i+1]
            else:
                current_val = nums[i]
                current_list = nums[i:i+1]
                L = i
                if current_val > best_val:
                    best_val = current_val
                    best_list = current_list
                #end
            #end
        #end
    #end
    return best_val, best_list
#end

def maxSubArray(nums):
    best_val = nums[0]
    current_val = 0
    for i in nums:
        if current_val < 0:
            current_val = 0
        #end
        best_val = max(best_val,current_val+i)
        current_val += i
    #end
    return best_val
#end

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([1]))
print(maxSubArray([5,4,-1,7,8]))