# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 20:42:03 2017

@author: Crystal
思路一：可以设置一个标志位，在标志位中将数字为0-n的状态表示出来，然后从第一个位置开始对这个标志位进行遍历找出第一个值为False的位置即为输出值。
思路二：先对这个列表按照位置i与数字i+1进行匹配排序，待所有位置关系确定后找出第一个不符合位置和值匹配关系的位置，输出i+1。
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==0:
            return 1
        seen=[False]*(n+1)
        for i in xrange(n):
            if nums[i]>0 and nums[i]<=n:
                seen[nums[i]]=True
            
        for i in xrange(1,n+1):
            if seen[i]==False:
                print i
                return
        print n+1
            

        

if __name__=='__main__':
    sol=Solution()
    sol.firstMissingPositive([1])