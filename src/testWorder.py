import sys
import nose
import logging
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises
import strategy_eng
import strategy_heb
import logger
import sorter
import Worder
class TestWorder():
  def setUp(self):
      self.logger=logger.Loggerf()
      self.dict = dict()
      self.filename="../data/words_80day10.txt"
      self.lines=7900
      self.level=5
      self.strategy= strategy_eng.StrategyEng(logger.Loggerf())
      self.worder=None
  def tearDown(self):
      self.dict.clear()

  def iteratefirstWords(self,level):
    stringa = ""
    for word in self.worder.itrerate_words(level):
      stringa = stringa + word + " "
      if (len(stringa) > 50): break
    return stringa


  def createWorder(self):
      worder = Worder.Worder(logger.Loggerf(), self.filename, self.dict,self.strategy )
      return worder

  def taestEng(self):
    self.worder = self.createWorder()
    self.worder.createDST(self.lines)
    stringa=self.iteratefirstWords()
    print "stringa:",stringa
    self.logger.log(logging.INFO, stringa)


  def testHeb(self):
     self.filename = "../data/words_guliver.txt"
     self.lines=5
     self.level=10
     self.strategy = strategy_heb.StrategyHeb(logger.Loggerf())
     self.worder = self.createWorder()
     self.worder.createDST(self.lines)

     stringa = self.iteratefirstWords(self.level)
     #print "stringa:", stringa
     self.logger.log(logging.INFO, stringa)


if __name__=="__main__":
    #logging.getLogger().setLevel(logging.INFO)
    #logging.log(logging.DEBUG,logging._levelNames)
    #logger=logger.Logger()
    test=TestWorder()
    #logging.log(logging.ERROR, logging._levelNames)
    module_name = sys.modules[__name__].__file__
    logging.debug("running nose for package: %s", module_name)

    result = nose.run(argv=[sys.argv[0],module_name,'-v'])

    logging.info("all tests ok: %s", result)