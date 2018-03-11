# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 14:22:12 2017

@author: Crystal
"""

from collections import defaultdict
#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        treeMap=defaultdict(list)
        
        def recursion(root):
            if not root:
                res='#'
            else:
                res='%s%s%s'%(root.val,recursion(root.left),recursion(root.right))
                treeMap[res].append(root)
            return res
        
        recursion(root)
        
        return [v[0] for v in treeMap.values() if len(v)>1]
                        
        
        
        
        