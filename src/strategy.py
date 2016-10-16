import logging
import logger
import itertools
import string

from StrategyWriter import StrategyWriter
class Strategy(object):
    def __init__(self,logger):
       self.logger=logger
       self.pairs=[]
       self.charStart=''
       self.charEnd=''
       self.seperator = ' '
       #self.strip='0123456789*.,:-?!;()[]\n"' TODO
       self.strip=string.punctuation+string.digits+"\n"
       self.triplets=[]
       self.writer = StrategyWriter(self.logger)
    def info(self):
        self.logger.log(logging.DEBUG, self.pairs)
    def align(self, word):
        #word_ret = word.strip(self.strip).strip(self.seperator)
        word_ret= word.translate(None,self.strip+self.seperator)  #TODO RE
        word_ret = word_ret.lower()
        return word_ret
    def index(self, word):
        word_len = len(word)
        if word_len < 3:
            return None
        return word[0:3]
    def levelToTriplets(self,level):
         stringi=""
         for i in xrange(0,level):
            stringi=stringi+self.pairs[i]

         permutations=itertools.permutations(stringi,3)
         return permutations
    def levelToSet(self,level):
        setk=set()
        for i in xrange(0, level ):
            setk=setk.union(set(self.pairs[i]))
        return setk

    def toSet(self,item):
        seta=set(item)
        return seta

if __name__=="__main__":
  pass