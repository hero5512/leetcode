# -*- coding: utf-8 -*-
"""
Created on Fri Jun 09 16:19:09 2017

@author: Crystal
"""

class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        seen=[False]*n
        step=0
        ans=0
        for i in xrange(n):
            while not seen[i]:
                seen[i]=True
                i,step=nums[i],step+1
            ans=max(step,ans)
            step=0
        print ans
           
if __name__=='__main__':
    sol=Solution()
    sol.arrayNesting([0,2,1])
    