# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 09:51:19 2017

@author: Crystal
"""
import Queue
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
#    先序遍历递归实现
#    def addOneRow(self, root, v, d):
#        """
#        :type root: TreeNode
#        :type v: int
#        :type d: int
#        :rtype: TreeNode
#        """
#        return self.preOrder(root, v, d, 1, 0)
#        
#    def preOrder(self, root, v, d, level, direction):
#        if level==d:
#            node=TreeNode(v)
#            if direction==0:
#                node.left=self.preOrder(root, v, d, level+1, 0)
#            else:
#                node.right=self.preOrder(root, v, d, level+1, 1)
#            return node
#        if root==None:
#            return None
#        root.left=self.preOrder(root.left, v, d, level+1, 0)
#        root.right=self.preOrder(root.right, v, d, level+1, 1)
#        return root
#   层次遍历
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d==1:
            newNode=TreeNode(v)
            newNode.left=root
            return newNode
        q=Queue.Queue()
        q.put(root)
        level=1;
        while q.not_empty:            
            size=q.qsize();
            while size>0:                
                cur=q.get()
                print cur.val
                if level==d-1:
                    leftNode=TreeNode(v)
                    rightNode=TreeNode(v)
                    leftNode.left=cur.left
                    rightNode.right=cur.right
                    cur.left=leftNode
                    cur.right=rightNode   
                else:
                    if cur.left!=None:
                        q.put(cur.left)
                    if cur.right!=None:
                        q.put(cur.right)
                size-=1        
            
            level+=1
            if level==d:
                return root
        
                
            
        
if __name__=="__main__":
    root=TreeNode(4)
    root.left=TreeNode(2)
    root.right=TreeNode(6)
    root.left.left=TreeNode(3)
    root.left.right=TreeNode(1)
    root.right.left=TreeNode(5)
    sol=Solution()
    root=sol.addOneRow(root,1,1)
    print root.val
#    print root.right.val