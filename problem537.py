# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 17:51:45 2017

@author: Crystal
"""

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x=self.parseComplex(a)
        y=self.parseComplex(b)

        return str(x[0]*y[0]-x[1]*y[1])+'+'+str(x[0]*y[1]+x[1]*y[0])+'i'
        
    def parseComplex(self ,s):
        l=[int(x) for x in s[:-1].split('+')]
        return l 
        

if __name__=='__main__':
    sol=Solution()
    sol.complexNumberMultiply('1+-1i','1+-1i')

#
#class Solution(object):
#    def complexNumberMultiply(self, a, b):
#        """
#        :type a: str
#        :type b: str
#        :rtype: str
#        """
#        x=self.parseComplex(a)
#        y=self.parseComplex(b)
#        real=str(x[0]*y[0]-x[1]*y[1])
#        imagin=str(x[0]*y[1]+x[1]*y[0])+'i'
#        if real=='0' and imagin=='0i':
#            return ''
#        elif real!='0' and imagin!='0i':
#            return real+'+'+imagin
#        elif real!='0' and imagin=='0i':
#            return real
#        elif real=='0' and imagin!='0i':
#            return imagin
#    def parseComplex(self ,s):
#        l=[int(x) for x in s[:-1].split('+')]
#        return l 