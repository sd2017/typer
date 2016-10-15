import logging
from strategy import Strategy as Strategy
import logger
class StrategyEng(Strategy):
    def __init__(self,logger):
       super(StrategyEng,self).__init__(logger)
       self.pairs=["jf","kd","ls","ca","nt","iv","me","hr","go","bp","qu","wn","cx","yz"]
       self.charStart='a'
       self.charEnd='z'
       self.seperator=' '




    def info(self):
        self.logger.log(logging.DEBUG, self.pairs)

if __name__=="__main__":
    #logger=logger.Logger()
    tmp=StrategyEng(logger.Loggerf())
    tmp.info()