# -*- coding: utf-8 -*-
"""
Created on Thu Mar 02 19:30:26 2017

@author: Crystal

1、字母频数相同没有顺序，相同字母放在一起
2、大小写字母不同
3、频数由高到低
注意：python中的字典是没有顺序的
"""
from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        c1,c2=Counter(s),{}
        #print c
        for k,v in c1.items():
            c2.setdefault(v,[]).append(k*v)
#        res=""
#        for i in range(len(s), -1, -1):
#            if i in c2:
#               res=res+"".join(c2[i])
        print "".join(["".join(c2[i]) for i in range(len(s),-1,-1) if i in c2])
if __name__=='__main__':
    sol=Solution()
    sol.frequencySort("Tree")