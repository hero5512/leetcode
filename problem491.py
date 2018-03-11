# -*- coding: utf-8 -*-
"""
Created on Thu May 11 16:16:01 2017
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
@author: Crystal
"""

class Solution(object):
#    def findSubsequences(self, nums):
#        """
#        :type nums: List[int]
#        :rtype: List[List[int]]
#        """
##        res=[]
##        sorted(nums)
##        temp=[]
##        for i in xrange(len(nums)):
##            temp.append(nums[i])
##            if len(temp)>=2:
##                res.append(temp[:])
##                
##        for i in xrange(len(nums)):
##            print i
##        print res
#        class Solution(object):
#    def findSubsequences(self, nums):
#        """
#        :type nums: List[int]
#        :rtype: List[List[int]]
#        """
#        ans = set()
#        def DFS(ind, result):
#            if len(result)>=2:
#                ans.add(tuple(result))
#            
#            for i in range(ind, len(nums)):
#                if not result or nums[i]>=result[-1]:
#                    result.append(nums[i])
#                    DFS(i+1, result)
#                    result.pop()
#        DFS(0, [])
#        print map(list, ans)
    def findSubsequences(self, nums):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            subs = {()}
            for num in nums:
                print {sub + (num,) for sub in subs if not sub or sub[-1] <= num}
                subs |= {sub + (num,) for sub in subs if not sub or sub[-1] <= num}
            return [sub for sub in subs if len(sub) >= 2]        
            

if __name__=='__main__':
    sol=Solution()
    sol.findSubsequences([4, 6, 7, 7])
