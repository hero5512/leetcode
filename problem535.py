# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 13:50:44 2017

@author: Crystal
"""

class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        
if __name__=='__main__':
    codec=Codec()
    
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))