"""
Is a Text Valid Palindrome
==========================

@author: mhtehrani
November 05, 2021
https://github.com/mhtehrani

"""

def isPalindrome(s):
    s = s.lower()
    string = str()
    for i in s:
        if i.isalnum():
            string += i
        #end
    #end
    
    if string == string[::-1]:
        return True
    else:
        return False
    #end
#end

print(isPalindrome("A man, a plan, a canal: Panama"))
