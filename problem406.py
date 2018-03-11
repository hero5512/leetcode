# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 09:36:36 2017

@author: LvQ
思路：1、首先根据h的大小从大到小排序，然后如果h值相等那么对k从小到大排序
2、最后从已排序的第一个(h,k)开始向结果序列根据k的大小插入
"""

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        res=[]
        if not people:
            return res;
        for i in xrange(1,len(people)):
            j=i-1
            p=i
            h=people[i][0]
            k=people[i][1]
            while h>=people[j][0] and j>=0 and p>=0:
                if h==people[j][0]:
                    while k<people[j][1] and j>=0 and p>=0 and h==people[j][0]:
                        a=people[j]
                        people[j]=people[p]
                        people[p]=a
                        j-=1
                        p-=1
                    break
                else:
                    a=people[j]
                    people[j]=people[p]
                    people[p]=a
                    
                j-=1
                p-=1
                
        for p in people:
            res.insert(p[1],p)
        return res
#        people=sorted(people,key=lambda x:x[1])
#        people=sorted(people,key=lambda x:-x[0])
#
#        res=[]
#        for p in people:
#            res.insert(p[1],p)
#        return res            
        

if __name__=='__main__':
    sol=Solution()
    sol.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])