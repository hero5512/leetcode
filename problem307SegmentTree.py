# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 21:43:35 2017

@author: Crystal
"""
class Node(object):
    def __init__(self, start, end):
        self.start=start
        self.end=end
        self.value=0
        self.right=None
        self.left=None  
    
    

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums=nums
        
        self.root=self.build(nums,0,len(nums)-1)
        
        
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        delta=val-self.nums[i]
        self.nums[i]=val
        self.updateValue(self.root, i,delta)
         
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.query(self.root,i,j)
    
    def query(self,root,i,j):
        
        if root.start==i and root.end==j:
            return root.value
        mid=(root.start+root.end)/2
        
        if j<=mid:
            return self.query(root.left,i,j)
        elif i>=mid+1:
            return self.query(root.right,i,j)
        else:
            return self.query(root.left,i,mid)+self.query(root.right,mid+1,j)
        
        
      
    
    def build(self, arr, i, j):
        
        if i==j:
            root=Node(i,j)
            root.value=arr[i]
            
            return root
        elif i>j:
            return None
            
        else:
            root=Node(i,j)
            mid=(i+j)/2
            root.left=self.build(arr,i,mid)
            root.right=self.build(arr,mid+1,j)
            root.value=root.left.value+root.right.value
            return root
            
    def updateValue(self, root, i, delta):
        
        if root.start==i and root.end==i:
            root.value=delta+root.value
            return 
        mid=(root.start+root.end)/2
        root.value=delta+root.value
        if i<=mid:
            #root.left.value=root.left.value+delta
            self.updateValue(root.left, i, delta)
            
        elif i>=(mid+1):
            #root.right.value=root.right.value+delta
            self.updateValue(root.right, i, delta)
            
        
        
                     
if __name__=="__main__":
    sol=NumArray([7,2,7,2,0])
    print sol.sumRange(0,2)
    print sol.update(4,6)
    print "update 4 6"
    print sol.sumRange(0,0)
    print sol.sumRange(1,1)
    print sol.sumRange(2,2)
    print sol.sumRange(3,3)
    print sol.sumRange(4,4)
    print sol.update(0,2)
    print sol.update(0,2)
    print "update 0 2"
    print sol.sumRange(0,0)
    print sol.sumRange(1,1)
    print sol.sumRange(2,2)
    print sol.sumRange(3,3)
    print sol.sumRange(4,4)
    print "update 0 9"
    print sol.update(0,9)
    
    print sol.sumRange(0,0)
    print sol.sumRange(1,1)
    print sol.sumRange(2,2)
    print sol.sumRange(3,3)
    print sol.sumRange(4,4)
    #print sol.sumRange(0,4)
    print sol.update(3,8)
    print sol.sumRange(0,4)
    print sol.update(4,1)
    print sol.sumRange(0,3)
    print sol.sumRange(0,4)
    print sol.update(0,4)
#    sol=NumArray([9,2,7,8,6])
#    print sol.sumRange(0,4)
#    sol.update(1,7)
#    print sol.sumRange(0,4)