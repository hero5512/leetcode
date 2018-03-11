# -*- coding: utf-8 -*-
"""
Created on Wed Jun 07 19:28:06 2017

@author: Crystal
"""
from collections import OrderedDict
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.key_val={}
        self.key_fre={}
        self.fre_key={}
        self.min=-1
        
        
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key_val:
            return -1
        frequency=self.key_fre[key]
        self.key_fre[key]=frequency+1
        del self.fre_key[frequency][key]
        if frequency==self.min and len(self.fre_key[frequency])==0:
            self.min+=1
#       如果fre_key中有键为frequency+1的
        if (frequency+1) not in self.fre_key:
            self.fre_key[frequency+1]=OrderedDict()
        self.fre_key[frequency+1][key]=-1
        return self.key_val[key]
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity<=0:
            return
        if key in self.key_val:
            self.key_val[key]=value
            self.get(key)
            return
#        当存储空间满了去掉最近最近不常使用的缓存页
        if len(self.key_val)>=self.capacity:
            remove=self.fre_key[self.min].popitem(last=False)[0]
            del self.key_fre[remove]
            del self.key_val[remove]
        self.min=1
        self.key_val[key]=value
        self.key_fre[key]=1
        if self.min not in self.fre_key:
            self.fre_key[1]=OrderedDict()
        self.fre_key[1][key]=-1
        
            
if __name__=='__main__':
    cache=LFUCache(2)
    cache.put(1, 1);
    print cache.fre_key
    print cache.key_fre
    print cache.key_val
    print '当前最小值:',cache.min
    cache.put(2, 2);
    print cache.fre_key
    print cache.key_fre
    print cache.key_val
    print '当前最小值:',cache.min
    print cache.get(1);       # returns 1
    print cache.fre_key
    print cache.key_fre
    print cache.key_val
    print '当前最小值:',cache.min
    cache.put(3, 3);    # evicts key 2
    print cache.fre_key
    print cache.key_fre
    print cache.key_val
    print '当前最小值:',cache.min
    cache.get(2);       # returns -1 (not found)
    print cache.fre_key
    print cache.key_fre
    print cache.key_val
    print '当前最小值:',cache.min
    cache.get(3);       # returns 3.
    print cache.fre_key
    print cache.key_fre
    print cache.key_val
    print '当前最小值:',cache.min
    cache.put(4, 4);    # evicts key 1.
    print cache.fre_key
    print cache.key_fre
    print cache.key_val
    cache.get(1);       # returns -1 (not found)
    print cache.fre_key
    print cache.key_fre
    print cache.key_val
    cache.get(3);       # returns 3
    print cache.fre_key
    print cache.key_fre
    print cache.key_val
    cache.get(4);       # returns 4
    print cache.fre_key
    print cache.key_fre
    print cache.key_val
                         
            
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)