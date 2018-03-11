# -*- coding: utf-8 -*-
"""
Created on Tue Dec 05 11:29:22 2017

@author: Crystal
"""

class Solution(object):
    def replaceWords(self, dict, sentence):
        
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        trie=Trie()
        trie.build(dict)
        #    将句子转换为前缀词输出
        return trie.search(sentence)
        
 
     
#字典树节点
class TrieNode(object):
    def __init__(self):
        self.isEnd=False
        self.son=[None]*26
        self.val=None
        

class Trie(object):
    def __init__(self):
        self.root=TrieNode()
#    创建字典树
    def build(self,dictionary):
        for i in dictionary:
            self.insert(i)
        
#    插入一个单词
    def insert(self,word):
        if word==None:
            return
        node=self.root
        for i in xrange(len(word)):
            pos=ord(word[i])-ord('a')
            if not node.son[pos]:
                node.son[pos]=TrieNode()
                node.son[pos].val=word[i]
            node=node.son[pos];
        node.isEnd=True
        
#    对句子中前缀提取    
    def search(self,sentence):
       res=""   
       words=sentence.split()
       print words
       for word in words:
           cur=self.root
           temp=""
           for i in xrange(len(word)):
               char=word[i]
               temp+=char
               pos=ord(char)-ord('a')
               if not cur.son[pos] and not cur.isEnd:
                   res=res+word
                   break
               elif cur.son[pos] and cur.son[pos].isEnd:
                   res=res+temp
                   break
               elif cur.son[pos] and not cur.son[pos].isEnd:
                   if i==len(word)-1:
                       res=res+temp
                   cur=cur.son[pos]
               
           res=res+' '
       return res.strip()        
#    def search(self,sentence):
#        res=""
#        words=sentence.split()
#        cur=self.root
#        for word in words:
#            temp=""
#            for c in word:
#                temp=temp+c
#                pos=ord(c)-ord('a')
#                if cur.son[pos]:
#                    if cur.son[pos].isEnd:
#                        res+=temp
#                        break
#                    cur=cur.son[pos]
#                else:
#                    res+=word
#                    break
##            res+=word    
#            res+=' '
#          
#        return res
       
if __name__=='__main__':
    
    sol=Solution()
#    print sol.replaceWords(["e","k","c","harqp","h","gsafc","vn","lqp","soy","mr","x","iitgm","sb","oo","spj","gwmly","iu","z","f","ha","vds","v","vpx","fir","t","xo","apifm","tlznm","kkv","nxyud","j","qp","omn","zoxp","mutu","i","nxth","dwuer","sadl","pv","w","mding","mubem","xsmwc","vl","farov","twfmq","ljhmr","q","bbzs","kd","kwc","a","buq","sm","yi","nypa","xwz","si","amqx","iy","eb","qvgt","twy","rf","dc","utt","mxjfu","hm","trz","lzh","lref","qbx","fmemr","gil","go","qggh","uud","trnhf","gels","dfdq","qzkx","qxw"],"ikkbp miszkays wqjferqoxjwvbieyk gvcfldkiavww vhokchxz dvypwyb bxahfzcfanteibiltins ueebf lqhflvwxksi dco kddxmckhvqifbuzkhstp wc ytzzlm gximjuhzfdjuamhsu gdkbmhpnvy ifvifheoxqlbosfww mengfdydekwttkhbzenk wjhmmyltmeufqvcpcxg hthcuovils ldipovluo aiprogn nusquzpmnogtjkklfhta klxvvlvyh nxzgnrveghc mpppfhzjkbucv cqcft uwmahhqradjtf iaaasabqqzmbcig zcpvpyypsmodtoiif qjuiqtfhzcpnmtk yzfragcextvx ivnvgkaqs iplazv jurtsyh gzixfeugj rnukjgtjpim hscyhgoru aledyrmzwhsz xbahcwfwm hzd ygelddphxnbh rvjxtlqfnlmwdoezh zawfkko iwhkcddxgpqtdrjrcv bbfj mhs nenrqfkbf spfpazr wrkjiwyf cw dtd cqibzmuuhukwylrnld dtaxhddidfwqs bgnnoxgyynol hg dijhrrpnwjlju muzzrrsypzgwvblf zbugltrnyzbg hktdviastoireyiqf qvufxgcixvhrjqtna ipfzhuvgo daee r nlipyfszvxlwqw yoq dewpgtcrzausqwhh qzsaobsghgm ichlpsjlsrwzhbyfhm ksenb bqprarpgnyemzwifqzz oai pnqottd nygesjtlpala qmxixtooxtbrzyorn gyvukjpc s mxhlkdaycskj uvwmerplaibeknltuvd ocnn frotscysdyclrc ckcttaceuuxzcghw pxbd oklwhcppuziixpvihihp")
    print sol.replaceWords(["cat", "bat", "rat"],"the ba cattle was rattled by the battery")