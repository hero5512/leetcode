# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 15:09:46 2017

@author: Crystal
"""
import math

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        result=str(math.log(n,3))
        if result.endswith('.0'):
            return True
        else:
            return False
        

if __name__=='__main__':
    sol=Solution()
    
    print sol.isPowerOfThree(9)