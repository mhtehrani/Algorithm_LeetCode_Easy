"""
Finding the Index of a string inside another String
===================================================

@author: mhtehrani
October 28, 2021
https://github.com/mhtehrani

"""

def strStr(haystack, needle):
    if not needle:
        return 0
    else:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
            #end
        #end
        
        return -1
    #end
#end

print(strStr("a", "a"))