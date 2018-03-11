# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 15:59:03 2017

@author: Crystal
"""

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        low=0
        mid=(length-1)/2
        high=length-1
        while low<high:
            if mid%2==1:
                if nums[mid]==nums[mid-1]:
                    low=mid+1  
                else:
                    high=mid-1  
            else:
                if nums[mid]==nums[mid-1]:
                    high=mid-2
                else:
                    low=mid+2 
            mid=(low+high)/2
 
        return nums[low]
                
if __name__=='__main__':
    sol=Solution()
    print sol.singleNonDuplicate([1,1,2,2,3,3,4,4,9])