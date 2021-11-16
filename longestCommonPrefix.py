"""
Longest Common Prefix
=====================

@author: mhtehrani
October 24, 2021
https://github.com/mhtehrani

"""

strs = ["flower","flow","flight","fr"]

LCP = strs[0]

for i in range(1,len(strs)):
    LCP = LCP[0:len(strs[i])]
    
    for j in range(min(len(LCP),len(strs[i]))):
        if LCP[j] != strs[i][j]:
            LCP = LCP[0:j]
            break
        #end
    #end
#end

print(LCP)