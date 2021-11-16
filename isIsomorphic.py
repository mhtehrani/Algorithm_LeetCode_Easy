"""
Isomorphic Strings
==================

@author: mhtehrani
November 11, 2021
https://github.com/mhtehrani

"""

def isIsomorphic(s, t):
    dic_l = {}
    dic_r = {}
    
    for i in range(len(s)):
        if s[i] in dic_l:
            if dic_l[s[i]] != t[i]:
                return False
            #end
        else:
            dic_l[s[i]] = t[i]
        #end
        
        if t[i] in dic_r:
            if dic_r[t[i]] != s[i]:
                return False
            #end
        else:
            dic_r[t[i]] = s[i]
        #end
    #end
    
    return True
#end

print(isIsomorphic("badc","baba"))