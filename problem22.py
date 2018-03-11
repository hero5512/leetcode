# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 16:21:47 2018

@author: Crystal
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l=[];
        self.backtrack(l,"",0,0,n)
        return l
            
    def backtrack(self,l,s,o,c,m):
        if len(s)==m*2:
            l.append(s)
            return
        if o<m:
            self.backtrack(l,s+'(',o+1,c,m)
        if c<o:
            self.backtrack(l,s+')',o,c+1,m)
            
if __name__=='__main__':
    sol=Solution()
    print sol.generateParenthesis(3)