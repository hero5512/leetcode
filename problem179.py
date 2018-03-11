# -*- coding: utf-8 -*-
"""
Created on Wed Apr 05 16:44:54 2017

@author: Crystal
思路：1、依次选择首位最大的元素放在第一位
2、如果首位相同就比较第二位，第二位大的依次排列，依次类推
[3, 30, 34, 5, 9]=9534330

1、python两个字符串居然可以比较大小
2、交换两个变量有个简便的形式
3、除此之外注意sort还可以自定义比较函数
4、判断字符串全为0的方法int("".join(num))
"""

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        if not any(nums):
            return "0"
        for i in xrange(len(nums)):
            for j in xrange(len(nums)-1,i,-1):                           
                if self.compare(nums[j],nums[j-1]):
                    nums[j],nums[j-1]=nums[j-1],nums[j]
        print "".join(map(str,nums))
        
    def compare(self,num1,num2):
        return str(num1)+str(num2)>str(num2)+str(num1)
        
if __name__=='__main__':
    sol=Solution()
    sol.largestNumber([3, 30, 34, 5, 9])