"""
Stack Data Structure
====================

@author: mhtehrani
November 06, 2021
https://github.com/mhtehrani

"""

# Definition for a binary tree node.
class MinStack:
    def __init__(self, val = []):
        self.val = val
        if val:
            self.min = val
        else:
            self.min = None
        #end
    #end
    
    def push(self, val: int) -> None:
        self.val.append(val)
        if self.min == None:
            self.min = val
        elif val < self.min:
            self.min = val
        #end
    #end

    def pop(self) -> None:
        if len(self.val) > 1:
            if self.min == self.val[len(self.val)-1]:
                self.min = min(self.val[0:(len(self.val)-1)])
            #end
        else:
            self.min = None
        #end
        return self.val.pop()
    #end
    
    def top(self) -> int:
        if self.val:
            return self.val[len(self.val)-1]
        else:
            return None
        #end
    #end

    def getMin(self) -> int:
        return self.min
    #end
#end

# Your MinStack object will be instantiated and called as such:
com = ["MinStack","push","push","push","getMin"]
vv = [[],[0],[1],[2],[]]
for i in range(len(com)):
    if com[i] == "MinStack":
        obj = MinStack()
    elif com[i] == "push":
        obj.push(vv[i][0])
    elif com[i] == "getMin":
        print(obj.getMin())
    # elif com[i] == 
        
obj.push(0)
obj.push(-3)
param_1 = obj.getMin()
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()