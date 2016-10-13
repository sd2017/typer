import logging
import strategy
import logger
class StrategyEng:
    def __init__(self,logger):
       self.logger=logger
       self.pairs=["jf","kd","ls","ca","nt","iv","me","hr","go","bp","qu","wn","cx","yz"]
       self.charStart='a'
       self.charEnd='z'
       self.seperator=' '
       self.strip=xrange('0','9')
    def align(self,word):
        word_ret=word.strip(self.strip).strip(self.seperator)
        word_ret=word_ret.lower()
        return word_ret

    def index(self,word):
        word_len = len(word)
        if word_len<3 :
            return None
        return  word[0:2]



    def info(self):
        self.logger.log(logging.DEBUG, self.pairs)

if __name__=="__main__":
    logger=logger.Logger()
    tmp=StrategyEng(logger.Logger())
    tmp.info()