# -*- coding: utf-8 -*-
"""
Created on Wed Jun 07 15:12:03 2017

@author: Crystal
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        j=len(nums)-k-1
        for i in xrange(0,(len(nums)-k)/2):
            a=nums[i]
            nums[i]=nums[j]
            nums[j]=a
            j-=1
        j=len(nums)-1
        for i in xrange(len(nums)-k,(2*len(nums)-k)/2):
            a=nums[i]
            nums[i]=nums[j]
            nums[j]=a
            j-=1
        j=len(nums)-1
        for i in xrange(0,len(nums)/2):
            a=nums[i]
            nums[i]=nums[j]
            nums[j]=a
            j-=1
        print nums
            
    
        
        
        
if __name__=="__main__":
    sol=Solution()
    sol.rotate([1,2,3,4,5,6,7],3)