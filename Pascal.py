"""
Pascal's Triangle
=================

@author: mhtehrani
November 05, 2021
https://github.com/mhtehrani

"""

def generate(numRows):
    pri = []
    if numRows == 1:
        pri.append([1])
    elif numRows == 2:
        pri.append([1])
        pri.append([1,1])
    else:
        pri.append([1])
        pri.append([1,1])
        for i in range(2,numRows):
            tem = [1]*(i+1)
            
            for j in range(0,i-1):
                tem[j+1] = pri[i-1][j]+pri[i-1][j+1]
            #end
            pri.append(tem)
        #end
    #end
    
    return pri
#end

print(generate(1))