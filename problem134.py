# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 19:57:33 2017

@author: Crystal
思路：从第一个加油站开始遍历，如果到达下一个加油站当前油量小于0，
则无法从当前选择
"""
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start=len(gas)-1
        end=0
        balance=gas[start]-cost[start]
        
        while start>end:
            if balance>0: 
                balance+=gas[end]-cost[end]
                end+=1
            else:
 
                start-=1
                balance+=gas[start]-cost[start]
        return start if balance>=0 else -1
                
            
            
        
        
        
if __name__=='__main__':
    sol=Solution()
    print sol.canCompleteCircuit([6,1,4,3,5],[3,8,2,4,2])