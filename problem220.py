# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 08:52:17 2017

@author: Crystal
"""
import collections;
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
#        length=len(nums)
#        if length<=1 or t<0 or k<1:
#            return False
#        for i in xrange(0,length): 
#            loop=i+k+1 if i+k+1<=length else length
#            
#            for j in xrange(i+1,loop): 
#                if abs(nums[i]-nums[j])<=t and abs(i-j)<=k:
#                    return True
#        return False
        if k < 1 or t < 0:
            return False
        numDict = collections.OrderedDict()
        for x in range(len(nums)):
            key = nums[x] / max(1, t)
            for m in (key, key - 1, key + 1):
                if m in numDict and abs(nums[x] - numDict[m]) <= t:
                    return True
            numDict[key] = nums[x]
            if x >=  k:
                numDict.popitem(last=False)
        return False

if __name__=="__main__":
    sol=Solution()
    print sol.containsNearbyAlmostDuplicate([-3,3],2,4)
    