# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 21:34:03 2017

@author: Crystal
"""

class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        if len(b)==1:
            return a**b[0]
            
        pre=((a**b[0])**10)%1337
        for i in xrange(1,len(b)):
            cur=a**b[i]
            if i==(len(b)-1):
                return (pre*cur)%1337
            pre=((pre*cur)**10)%1337
            
                
            

if __name__=='__main__':
    sol=Solution()
    print sol.superPow(2,[1,0,3,2,4,3,9,0,1,2,5])
    