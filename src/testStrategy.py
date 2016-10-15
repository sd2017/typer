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
class TestStrategy():
    def __init__(self):
      self.logger=logger.Loggerf()
    def setUp(self):
      self.strategy=strategy_eng.StrategyEng(self.logger)
    def tearDown(self):
      del self.strategy

    def test_eng_triplets2(self):
        triplets3=[]
        triplets= self.strategy.levelToTriplets(2)
        #triplets2 = ''.join([`trip` for trip in triplets]) #TODO
        for trip in triplets:
           triplets3.append(''.join(trip))
        self.logger.log(logging.INFO,triplets3)


    def test_eng_set2(self):
      setk = self.strategy.levelToSet( 2)
      self.logger.log(logging.INFO, setk)


    def test_eng_set3(self):
        setk = self.strategy.levelToSet(3)
        self.logger.log(logging.INFO, setk)


    def test_eng_set4(self):
        setk = self.strategy.levelToSet(4)
        self.logger.log(logging.INFO, setk)


    def test_eng_set5(self):
        setk = self.strategy.levelToSet(5)
        self.logger.log(logging.INFO, setk)


    def test_eng_set6(self):
        setk = self.strategy.levelToSet(6)
        self.logger.log(logging.INFO, setk)


    def test_eng_set7(self):
        setk = self.strategy.levelToSet(7)
        self.logger.log(logging.INFO, setk)


if __name__=="__main__":
    #logging.getLogger().setLevel(logging.INFO)
    #logging.log(logging.DEBUG,logging._levelNames)
    #logger=logger.Logger()
    test=TestStrategy()
    #logging.log(logging.ERROR, logging._levelNames)
    module_name = sys.modules[__name__].__file__
    logging.debug("running nose for package: %s", module_name)

    result = nose.run(argv=[sys.argv[0],module_name,'-v'])

    logging.info("all tests ok: %s", result)