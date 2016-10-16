import linecache
import strategy
import strategy_eng
import logger
import logging

class Sorter:
    def __init__(self,loggeri,filename,dicti,strategy):
        self.logger=loggeri
        self.filename=filename
        self.dicta=dicti
        self.line="the most noticeable members of the Reform Club, though he seemed"
        self.strategy=strategy
        self.linecache=linecache
        self.linenum=1

    def line_read(self):
        self.line=self.linecache.getline(self.filename,self.linenum)
        self.linenum=self.linenum+1

    def line_to_dictionary(self):
        words = self.line.split(self.strategy.seperator)
        for word in words:
           word_aligned=self.strategy.align(word)
           word_index= self.strategy.index(word_aligned)
           #self.logger.log(logging.ERROR, "{}".format( word_aligned))
           # TODO self.logger.log(logging.DEBUG, "{}:{}".format( word_index,word_aligned))
           if (None != word_index):
               self.dicta.setdefault(word_index, set()).add(word_aligned)


    def sort(self,num):
        for i in range(0,num):
            self.line_read()
            self.line_to_dictionary()
    def info(self):
        self.logger.log(logging.INFO, self.dicta)
        self.logger.log(logging.INFO, self.dicta.keys())

if __name__=="__main__":
    sorter=Sorter(logger.Loggerf(),"../data/words_80day10.txt",{},strategy_eng.StrategyEng(logger.Logger()))
    sorter.line_to_dictionary()
    sorter.info()