# -*- coding: utf-8 -*-

import logging
import logger
class StrategyHeb:
    def __init__(self,logger):
       self.logger=logger
       self.pairs=["חכ","לג"," ךד","בש","נט","ןה","צק","יר","עם","נפ","ו","מ","בס","טז"]

    def info(self):
        self.logger.log(logging.DEBUG, self.pairs)

if __name__=="__main__":
    logger=logger.Logger()
    tmp=StrategyHeb(logging)
    tmp.info()