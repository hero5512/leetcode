# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 17:18:31 2017

@author: Crystal
"""

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        island=0
        neighbor=0
        for i in xrange(len(grid)):
            
            for j in xrange(len(grid[i])):
                if grid[i][j]==1:
                    island+=1
                    if j<len(grid[i])-1 and grid[i][j+1]==1:
                        neighbor+=1
                    if i<len(grid)-1 and grid[i+1][j]==1:
                        neighbor+=1
                        
                        
        return island*4-neighbor*2      
                    
            

if __name__=='__main__':
    sol=Solution()
    print sol.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])