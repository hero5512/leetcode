# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 16:57:23 2017

@author: Crystal
"""

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.isupper() or word.islower() or word.istitle()
