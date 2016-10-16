import sys
import logging
import logger
import sorter
import strategy_eng
import marshal
import cPickle
import copy
import gc
import os
import codecs


class Worder:
    suffixes = {"DST": ".dst", "TXT": ".txt", "LVL": ".txt"}

    def __init__(self, loggeri, filename, dict, strategy):
        self.dict = dict
        self.logger = loggeri
        self.filename = filename
        self.strategy = strategy
        self.level = 7

    def toFileDST(self):
        filename = self.filename + Worder.suffixes["DST"]

        with open(filename, 'wb') as handle:
            gc.disable()
            cPickle.dump(self.dict, handle, cPickle.HIGHEST_PROTOCOL)
            gc.enable()
            handle.close()

    def deleteFileDST(self):
        filename = self.filename + Worder.suffixes["DST"]
        try:
            os.remove(filename)
        except:
            pass

    def fromFileDST(self):
        filename = self.filename + Worder.suffixes["DST"]
        try:
            with open(filename, 'rb') as handle:

                gc.disable()
                self.dict = cPickle.load(handle)
                # TODO dict=cPickle.load( handle)
                # copy.deepcopy(self.dict,dict)
                gc.enable()
                handle.close()
        except EOFError:
            handle.close()
        except cPickle.PickleError:
            handle.close()
        except IOError:
            pass
        gc.enable()

    def fromFileTXT(self, lines):
        sorterl = sorter.Sorter(self.logger, self.filename, self.dict, self.strategy)
        sorterl.sort(lines)
        self.logger.log(logging.DEBUG, ("fromFileTXT", dict))

    def createDST(self, lines):
        self.fromFileDST()
        if (len(self.dict.keys()) < 3):
            self.fromFileTXT(lines)
            self.toFileDST()

    def itrerate_words(self, level):
        self.level = level
        setk = self.strategy.levelToSet(self.level)
        keys = self.dict.keys()
        self.logger.log(logging.DEBUG, "SHOSHAN check translations of  key,setk, itrerate_words:level=%s", level)
        self.logger.log(logging.DEBUG, "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
        for key in keys:
            self.logger.log(logging.DEBUG, "kkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
            self.logger.log(logging.DEBUG, "key:%s", self.strategy.toSet(key))
            self.logger.log(logging.DEBUG, "level set %s", setk)
            if self.strategy.toSet(key).issubset(setk):
                self.logger.log(logging.DEBUG, "subset of:%s", setk)
                for word in self.dict[key]:
                    if (set(word).issubset(setk)):
                        self.logger.log(logging.DEBUG, "found :%s", word)
                        yield word

    def toFileLVL(self, level):
        filename = self.filename + '.' + str(level).zfill(2) + Worder.suffixes["LVL"]
        with open(filename, 'wb') as handle:  # TODO
            writer = self.strategy.writer.getwriter(handle)
            for i,word in zip(range(0,300) ,self.itrerate_words(level)):
                    self.logger.log(logging.DEBUG,"toFileLVL call:%s", word)
                    writer.write(word)
                    writer.write(" \n")
                    self.logger.log(logging.DEBUG, "toFileLVL write:%s", word)
                    if i>250:break
            handle.flush()
            handle.close()

    def toFileLVLNoWriter(self, level):
        filename = self.filename + '.' + (str(level).zfill(3)) + Worder.suffixes["LVL"]
        with open(filename, 'wb') as handle:  # TODO
            # with codecs.open("filename", "w", "utf-32") as handle:
            # writer=codecs.StreamWriter(handle)
            writer = codecs.getwriter('utf - 8')(handle)
            stringa = ""
            for word in self.itrerate_words(level):
                stringa = stringa + word + " "
                if (len(stringa) > 50):
                    self.logger.log(logging.DEBUG, "stringa write:%s", stringa)
                    # handle.write(stringa)
                    # handle.write("\n") #TODO
                    writer.write(stringa)
                    writer.write("\n")
                    stringa = ""
            handle.flush()
            handle.close()


if __name__ == "__main__":
    dict = {}
    worder = Worder(logger.Loggerf(), "../data/words_80day10.txt", dict, strategy_eng.StrategyEng(logger.Loggerf()))
    worder.createDST()
    for level in xrange(5, 12):
        worder.toFileLVL(level)
        # worder.itrerate_words(10) #TODO
