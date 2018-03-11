# -*- coding: utf-8 -*-
"""
Created on Sat Jul 08 13:06:16 2017

@author: Crystal
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        h = len(nums) - 1
        if len(nums)==0 :
            return -1
        while l < h:
            m=(h+l)/2
            if nums[m] == target:
                print m
                return m
            if nums[l] > nums[m]:
                if target > nums[m] and target <= nums[h]:
                    l = m + 1
                else:
                    h = m - 1
                
            else:
                if target >= nums[l] and target < nums[m]:
                    h = m - 1
                else:
                    l = m + 1
#            return  nums[l]==target ? l : -1
        print l if nums[l]==target else -1
            
                    
              
        

if __name__=='__main__':
    sol=Solution()
    sol.search([5,1,3],3)