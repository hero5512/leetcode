# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 11:34:29 2017

@author: Crystal
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        str = s.strip()
        output=""
        index=len(str)
        p=index-1
        while index>0:
            if p > 0:
                if(str[p]!=' '):
                    p -= 1
                else:
                    output=output+str[p+1:index]+" "
                    while str[p]==' ':
                        p-=1
                    index=p+1
            else:
                output=output+str[p:index]
                index=p-1

        return output

if __name__=="__main__":
    sol=Solution()
    print sol.reverseWords("the sky is   blue");
    