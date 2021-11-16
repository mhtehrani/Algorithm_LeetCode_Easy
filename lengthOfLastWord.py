"""
The Length of the Last Word
===========================

@author: mhtehrani
October 30, 2021
https://github.com/mhtehrani

"""

def lengthOfLastWord(s):
    count = 0
    for i in range(len(s),0,-1):
        if s[i-1] != " ":
            count += 1
        elif count != 0:
            return count
        #end
    #end
    return count
#end

print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord("   fly me   to   the moon  "))
print(lengthOfLastWord("luffy is still joyboy"))
print(lengthOfLastWord("a"))
print(lengthOfLastWord("  "))