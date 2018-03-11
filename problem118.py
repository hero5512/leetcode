# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 15:09:21 2017

@author: Crystal
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res=[]
        if numRows==0:
            return res
        for i in xrange(numRows):
            cur=[]
            for j in xrange(i+1):
                if j==0 or j==i:
                    cur.append(1)
                else:
                    pre=res[i-1]
                    cur.append(pre[j-1]+pre[j])
            res.append(cur)
        print res

if __name__=='__main__':
    sol=Solution()
    sol.generate(5)