"""
Get the row of a Pascal's Triangle
==================================

@author: mhtehrani
November 05, 2021
https://github.com/mhtehrani

"""

def getRow(rowIndex):
    pri = []
    if rowIndex == 0:
        pri.append([1])
    elif rowIndex == 1:
        pri.append([1])
        pri.append([1,1])
    else:
        pri.append([1])
        pri.append([1,1])
        for i in range(2,rowIndex+1):
            tem = [1]*(i+1)
            
            for j in range(0,i-1):
                tem[j+1] = pri[i-1][j]+pri[i-1][j+1]
            #end
            pri.append(tem)
        #end
    #end
    
    return pri[rowIndex]
#end

print(getRow(3))