"""
Merge two non-decreasing Lists
==============================

@author: mhtehrani
October 31, 2021
https://github.com/mhtehrani

"""

def merge(nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = n+m-1
        while n > 0 and m > 0:
            if nums2[n-1] >= nums1[m-1]:
                nums1[i] = nums2[n-1]
                n -= 1
            else:
                nums1[i] = nums1[m-1]
                m -= 1
            #end
            i -= 1
        #end
        
        if n > 0:
            for i in range(n,0,-1):
                nums1[i-1] = nums2[n-1]
                n -= 1
            #end
        elif m > 0:
            for i in range(m,0,-1):
                nums1[i-1] = nums1[m-1]
                m -= 1
            #end
        #end
        return nums1
        
nums1 = [0]
m = 0
nums2 = [2]
n = 1
print(merge(nums1, m, nums2, n))