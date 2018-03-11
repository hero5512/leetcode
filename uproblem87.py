# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 08:52:24 2017

@author: Crystal
TODO 沒想出來
可以考虑用动态规划解决。。。。
"""

class Solution(object):
    def isScramble(self, s1, s2):
        n, m = len(s1), len(s2)
        if n != m or sorted(s1) != sorted(s2):
            return False
        if n < 4 or s1 == s2:
            return True
        f = self.isScramble
        for i in range(1, n):
            if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) or \
               f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
                return True
        return False

      
if __name__=='__main__':
    sol=Solution()
    sol.isScramble('great','rgtae')