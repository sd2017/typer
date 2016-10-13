
import logging
import logger
class StrategyHeb:
    def __init__(self,logger):
       self.logger=logger
       self.pairs=[]
       self.charStart=''
       self.charEnd=''
       self.seperator = ''
    def info(self):
        self.logger.log(logging.DEBUG, self.pairs)

if __name__=="__main__":
    logger=logger.Logger()
    tmp=StrategyHeb(logging)
    tmp.info()