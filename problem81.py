# -*- coding: utf-8 -*-
"""
Created on Sat Jul 08 12:54:27 2017

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
            return False
        while l < h:
            m=(h+l)/2
            if nums[m] == target:
             
                return True
            if nums[l] > nums[m]:
                if target > nums[m] and target <= nums[h]:
                    l = m + 1
                else:
                    h = m - 1
                
            elif nums[l] < nums[m]:
                if target >= nums[l] and target < nums[m]:
                    h = m - 1
                else:
                    l = m + 1
            else:
                l = l + 1
#            return  nums[l]==target ? l : -1
        return True if nums[l]==target else False

if __name__=='__main__':
    sol=Solution()
    print sol.search([1,3,1,1,1],3)
    