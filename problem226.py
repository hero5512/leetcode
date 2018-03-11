# -*- coding: utf-8 -*-
"""
Created on Wed Jul 05 16:55:38 2017

@author: Crystal
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """def invertTree(self, root):
        """
#        :type root: TreeNode
#        :rtype: TreeNode
    """
        if root==None or (root.left==None and root.right==None):
            
            return root
            
        root.right,root.left=root.left,root.right
        if root.right!=None:
            root.right=self.invertTree(root.right)
        if root.left!=None:
            root.left=self.invertTree(root.left)
        return root
        """
    def invertTree(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            
            if node:
                print node.val
                node.left, node.right = node.right, node.left
                stack.extend([node.right, node.left])
        return root
        

if __name__=='__main__':
    
    sol=Solution()
    n1=TreeNode(4)
    n2=TreeNode(2)
    n3=TreeNode(7)
    n4=TreeNode(1)
    n5=TreeNode(3)
    n6=TreeNode(6)
    n7=TreeNode(9)
    n1.left=n2
    n1.right=n3
    n2.left=n4
    n2.right=n5
    n3.left=n6
    n3.right=n7
    sol.invertTree(n1)
    print n1.left.val,n1.right.val,n2.left.val,n2.right.val,n3.left.val,n3.right.val
   
   
    