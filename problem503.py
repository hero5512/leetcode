# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:48:33 2017
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. 
The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, 
which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.
@author: Crystal
"""

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output,stack = [None]*len(nums),[]
        if not nums:
            return []
        
        for i in xrange(len(nums)):
            while stack and nums[stack[-1]]<nums[i]:
                j=stack.pop()
                output[j]=nums[i]
            stack.append(i)
        print stack
        for i in xrange(len(nums)):
            while stack and nums[stack[-1]]<nums[i]:
                j=stack.pop()
                output[j]=nums[i]
            
        while stack:
            output[stack.pop()]=-1
        return output

if __name__ == '__main__':
    sol = Solution()
    print sol.nextGreaterElements([1,1,1,1,1])
    