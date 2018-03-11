# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 09:05:18 2017

@author: Crystal
"""

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        cur = -1
        total = 0
        for i in timeSeries:
            if cur >= i:
                delta = duration - (cur - i + 1)
                total = total + delta
                cur = cur + delta
            else:
                total = total + duration
                cur = i + duration -1
        print total
        
        

if __name__=='__main__':
    sol=Solution()
    sol.findPoisonedDuration([1,4],2)