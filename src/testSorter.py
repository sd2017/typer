import unittest
import strategy_eng
import logger
import sorter
class TestSorter(unittest.TestCase):
  def setUp(self):
      self.sorter = sorter.Sorter("../data/words_80day10.txt", {}, strategy_eng.StrategyEng(logger.Logger()))
  def tearDown(self):
      del self.sorter
  def test_line(self):
      self.sorter.line_to_dictionary()
      self.sorter.info()

if __name__="__main__":
    test=TestSorter()
    unittest.main()