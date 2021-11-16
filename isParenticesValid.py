"""
Is Parentices Valid?
====================

@author: mhtehrani
October 24, 2021
https://github.com/mhtehrani

"""

def isValid(s):
    state = s[0]
    if s[0] == ')' or s[0] == '}' or s[0] == ']':
        return False
        # print(False)
    for i in range(1,len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            state += s[i]
        elif len(state) == 0:
            return False
        elif s[i] == ')':
            if state[len(state)-1] == '(':
                state = state[:-1]
            else:
                # print(False)
                return False
            #end
        elif s[i] == '}':
            if state[len(state)-1] == '{':
                state = state[:-1]
            else:
                # print(False)
                return False
            #end
        elif s[i] == ']':
            if state[len(state)-1] == '[':
                state = state[:-1]
            else:
                # print(False)
                return False
            #end
        #end
    #end
    
    if len(state) == 0:
        return True
    else:
        return False


s = '(){}}{'
print(isValid(s))