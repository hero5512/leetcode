# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 11:18:22 2017

@author: Crystal
"""

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """

        
        original=list(str(n))
        j=0
        
        for j in xrange(len(original)-1,0,-1):
            if original[j-1] < original[j] :
                break
            if j==1:
                j=j-1
        
        if j==0:
            return -1
        
        x=original[j-1]
        smallest=j
        for i in xrange(j+1,len(original)):
            if x<original[i]<=original[smallest]:
                smallest=i
                
        original[smallest],original[j-1]=original[j-1 ],original[smallest]
        
        temp=sorted(original[j:len(original)])
        original[j:len(original)]=temp
        res=int(''.join(original))
        if 0<res<=2147483647: 
            return res
        else:
            return -1
 
if __name__=='__main__':
    sol=Solution()
    print sol.nextGreaterElement(199999999999)