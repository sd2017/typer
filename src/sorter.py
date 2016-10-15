import logger
import linecache
import strategy
import strategy_eng
class Sorter:
    def __init__(self,filename,dict,strategy):
        self.filename=filename
        self.dict={}
        self.line="the most noticeable members of the Reform Club, though he seemed"
        self.strategy=strategy_eng.StrategyEng(logger.Logger())
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
           print word_index,":",word_aligned
           if (None != word_index):
               self.dict.setdefault(word_index,set()).add(word_aligned)


    def sort(self,num):
        for i in range(0,num):
            self.line_read()
            self.line_to_dictionary()
    def info(self):
        print self.dict

if __name__=="__main__":
    sorter=Sorter("../data/words_80day10.txt",{},strategy_eng.StrategyEng(logger.Logger()))
    sorter.line_to_dictionary()
    sorter.info()