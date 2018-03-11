# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 10:52:56 2017

@author: Crystal
"""

#class Solution(object):
#    def maxProduct(self, words):
#        """
#        :type words: List[str]
#        :rtype: int
#        """
#        length=len(words)
#        value=[0]*length;
#        maxlength=0
#        for i in xrange(length):
#            word=words[i]
#            for j in xrange(len(word)):
#                value[i]=value[i]|(1<<ord(word[j])-ord('a'))
#        for i in xrange(length):
#            for j in xrange(i+1,length):
#                temp=len(words[i])*len(words[j])
#                if value[i]&value[j]==0 and temp>maxlength:
#                   maxlength=temp 
#        return maxlength    
import itertools      
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        bits = {}
        for word in words:
            bit = 0
            for char in word:
                bit |= 1<<(ord(char) - 97)
                print bit
            bits[bit] = max(len(word), bits[bit]) if bit in bits else len(word)

        if len(bits) <= 1:
            return 0

        return max([bits[x] * bits[y] for x, y in itertools.combinations(bits, 2)
                    if x & y == 0] + [0])        
    
if __name__=='__main__':
    sol=Solution()
    print sol.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])
    print len("foo"),len("abcw")
    
    
    
