"""
Return the Two Indices That Sum to a Target
===========================================

@author: mhtehrani
November 07, 2021
https://github.com/mhtehrani

"""

def twoSum(numbers, target):
    i = 0
    j = len(numbers)-1
    while i<j:
        dummy = numbers[i]+numbers[j]
        if dummy == target:
            return [i+1,j+1]
        elif dummy < target:
            i += 1
        else:
            j -= 1
        #end
    #end
    
    return None
#end

print(twoSum([2,7,11,15],9))


