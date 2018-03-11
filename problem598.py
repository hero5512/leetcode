# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 09:38:24 2017

@author: Crystal
注意python多维数组赋初值这个坑
"""
class Solution(object):
    def maxCount(self, m, n, ops):
#        """
#        :type m: int
#        :type n: int
#        :type ops: List[List[int]]
#        :rtype: int
#        """
#        M=[[0]*n]*m
        if not ops:
            return m*n
            
        """
        方法一貌似不行
        M=[[0 for j in range(n)] for i in range(m) ]
        for op in ops:
            count=0
            for i in range(op[0]):
                for j in range(op[1]):
                    M[i][j]=M[i][j]+1
                    if M[i][j]==M[0][0]:
                        count+=1
        print count
        """
        
#        a=M[0][0]
#        count=0
#        for i in M:
#            for j in i:
#                if j==a:
#                    count+=1
#                elif j!=a:
#                    continue
        x=min([s[0] for s in ops])
        y=min([s[1] for s in ops])
        return x*y
        
if __name__=='__main__':
    sol=Solution()
    sol.maxCount(3,3,[[2,2],[3,3]])
    