import logger
import linecache
import strategy
import strategy_eng
class Sorter:
    def __init__(self,filename,dict,strategy):
        self.linecache= linecache.cache(filename)
        self.dict=dict
        self.line="the most noticeable members of the Reform Club, though he seemed"
        self.strategy=strategy_eng.StrategyEng(logger.Logger())
    def line_read(self):
        self.line=self.linecache.readline()

    def line_to_dictionary(self):
        words = self.line.split(self.strategy.seperator)
        for word in words:
           word_aligned=self.strategy.align(word)
           word_index= self.strategy.index(word_aligned)
           if (None != word_index)
               dict.
