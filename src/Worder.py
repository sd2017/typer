import sys
import logging
import logger
import sorter
import strategy_eng
import marshal
import cPickle
import copy
import gc


class Worder:
    suffixes = {"DST": ".dst", "TXT": ".txt"}

    def __init__(self, loggeri, filename, dict, strategy):
        self.dict = dict
        self.logger = loggeri
        self.filename = filename
        self.strategy = strategy

    def toFileDST(self):
        filename = self.filename + Worder.suffixes["DST"]

        with open(filename, 'wb') as handle:
            gc.disable()
            cPickle.dump(self.dict, handle, cPickle.HIGHEST_PROTOCOL)
            gc.enable()
            handle.close()

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
        except cPickle.PickleError:handle.close()
        except IOError:pass
        gc.enable()


    def fromFileTXT(self):
        sorterl = sorter.Sorter(self.logger, self.filename, dict, self.strategy)
        sorterl.sort(7900)
        print "fromFileTXT",dict

    def createDST(self):
        self.fromFileDST()
        if (len(dict.keys()) < 3):
            self.fromFileTXT()
            self.toFileDST()


if __name__ == "__main__":
    dict = {}
    worder = Worder(logger.Loggerf(), "../data/words_80day10.txt", dict, strategy_eng.StrategyEng(logger.Logger()))
    worder.createDST()
    print "main"
    print dict
