# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 11:22:56 2017
Given a singly linked list where elements are sorted in ascending order, 
convert it to a height balanced BST.
@author: Crystal
此题还可以用模拟树的中序遍历实现
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def sortedListToBST(self ,head ):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        l=[head.val]
        while head.next:
            head=head.next
            l.append(head.val)
        return self.convert2BST(l,0,len(l)-1)
        
    def convert2BST(self, l, start, end):
        """
        :type l: List
        :rtype: TreeNode
        """
        middle=(end+start)/2
        if end>start:
            tree=TreeNode(l[middle])
            tree.left=self.convert2BST(l,start,middle-1)
            tree.right=self.convert2BST(l,middle+1,end)
            return tree
        elif end==start:
            tree=TreeNode(l[middle])
            return tree
        else:
            return None
#/* 
# 模拟树的中序遍历递归版。 
#  */  
#116ms  
#class Solution {  
#public:  
#    TreeNode *sortedListToBST(ListNode* & head, int start, int end) {  
#        if (start > end) return NULL;  
#        int mid = start + (end - start) / 2;  
#        TreeNode* left = sortedListToBST(head, start, mid - 1);  
#        TreeNode* parent = new TreeNode(head->val);  
#        parent->left = left;  
#        head = head->next;  
#        TreeNode* right = sortedListToBST(head, mid + 1, end);  
#        parent->right = right;  
#        //levelorder_tra(parent);  
#        return parent;  
#    }  
#      
#    TreeNode *sortedListToBST(ListNode *head) {  
#        int length = 0;  
#        ListNode* node = head;  
#        while ( node != NULL) {  
#            length++;  
#            node = node->next;  
#        }  
#        return sortedListToBST(head, 0, length - 1);      
#    }  
#};          
if __name__=='__main__':
    sol=Solution()
    l=ListNode(0)
    sol.sortedListToBST(l)
#    sol.sortedListToBST([0,1,2,3,4,5,6,7,8,9])
        