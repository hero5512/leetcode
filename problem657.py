# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 21:00:32 2017

@author: Crystal
"""

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        vertical=0
        horizontal=0
        for i in xrange(len(moves)):
            if moves[i]=='D':
                vertical-=1
            elif moves[i]=='U':
                vertical+=1
            elif moves[i]=='L':
                horizontal-=1
            elif moves[i]=='R':
                horizontal+=1
        if vertical==0 and horizontal==0:
            return True
        else:
            return False
                
if __name__=='__main__':
    sol=Solution()
    