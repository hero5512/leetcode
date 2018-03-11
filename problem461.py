# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 18:44:10 2017

@author: Crystal
"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        distance=0
        while x or y:
            if(x%2 != y%2):
               distance=distance+1
            x=x>>1
            y=y>>1
        print distance

if __name__=='__main__':
    sol=Solution()
    sol.hammingDistance(1,4)       