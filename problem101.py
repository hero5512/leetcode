# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 15:41:33 2017

@author: Crystal
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.recursive(root,root.left,root.right)
    def recursive(self,root,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val==right.val and self.recursive(root,left.left,right.right) and self.recursive(root,right.left,left.right) 
        
        
if __name__=='__main__':
    sol=Solution()