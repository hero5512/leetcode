# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 11:00:35 2017

@author: Crystal
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        res=""
        return self.recursion(t,res)
        
        
    def recursion(self, root, res):
        if not root:
            return res
        res+=str(root.val)
        if root.left and root.right:
            res+="("
            res=self.recursion(root.left,res)
            res+=")"
            res+="("
            res=self.recursion(root.right,res)
            res+=")"
        elif not root.left and root.right:
            res+="()"
            res+="("
            res=self.recursion(root.right,res)
            res+=")"
        elif root.left and not root.right:
            res+="("
            res=self.recursion(root.left,res)
            res+=")"
        return res