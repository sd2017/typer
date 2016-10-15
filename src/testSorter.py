import sys
import nose
import logging
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises
import strategy_eng
import logger
import sorter
class TestSorter():
  def setUp(self):
      self.sorter = sorter.Sorter(logger.Loggerf(),"../data/words_80day10.txt", {}, strategy_eng.StrategyEng(logger.Logger()))
  def tearDown(self):
      del self.sorter
  def test_line(self):
      self.sorter.line_to_dictionary()
      self.sorter.info()
  def test_line5(self):
     self.sorter.sort(5)
     self.sorter.info()

  def test_line100(self):
       self.sorter.sort(100)
       self.sorter.info()

  def test_line7900(self):
        self.sorter.sort(7900)
        self.sorter.info()


if __name__=="__main__":
    #logging.getLogger().setLevel(logging.INFO)
    #logging.log(logging.DEBUG,logging._levelNames)
    #logger=logger.Logger()
    test=TestSorter()
    #logging.log(logging.ERROR, logging._levelNames)
    module_name = sys.modules[__name__].__file__
    logging.debug("running nose for package: %s", module_name)

    result = nose.run(argv=[sys.argv[0],module_name,'-v'])

    logging.info("all tests ok: %s", result)