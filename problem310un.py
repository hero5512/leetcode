# -*- coding: utf-8 -*-
"""
Created on Tue May 09 09:20:01 2017

@author: Crystal
可以考虑使用宽度优先遍历
Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
     0  1  2
      \ | /
        3
        |
        4
        |
        5
"""
from collections import deque
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
#        创建图结构
        
        tree={}
        res=[]
        if not edges:
            res.append(0)
            return res
        for edge in edges:
            if not tree.has_key(edge[0]):
                tree[edge[0]]=[]
            if not tree.has_key(edge[1]):
                tree[edge[1]]=[]
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])
        print tree
        leaves=[i for i in xrange(n) if len(tree.get(i))==1]
        print leaves
        
#        广度优先遍历
        for i in xrange(n):
            visited=[False]*n
            queue=deque([i])
            while queue:
                first=queue.popleft()
                visited[first]=True
                for node in tree[first]:
                    if not visited[node]:
                        queue.append(node)
                        print queue
        print res
            
if __name__=='__main__':
    sol=Solution()
    sol.findMinHeightTrees(6,[[0,1],[0,2],[0,3],[3,4],[4,5]])