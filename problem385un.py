# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 11:56:58 2017

@author: Crystal
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]

#    [123,[456,[789]]]

#        """

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        stack=[]
        res=NestedInteger()
        temp=""
        for i in xrange(len(s)):
            if s[i]=='[':
                stack.append(NestedInteger())
            elif s[i]==']':
                temp=""
                res=stack[-1]
            elif s[i]!=',':
                temp+=s[i]
            print temp
            res.setInteger(int(temp))
        
        
        return stack[0]
        

        
sol=Solution()
sol.deserialize("[123,[456,[789]]]")     