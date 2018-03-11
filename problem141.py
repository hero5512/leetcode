# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 16:46:50 2017

@author: Crystal
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None or head.next==None:
            return False
        if head==head.next.next:
            return True
            
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next 
            fast=fast.next.next
            if slow==fast:
                return True
                
        return False
        
        


    