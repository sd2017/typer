import codecs
import logging
import logger
from StrategyWriter import StrategyWriter
from StringIO import StringIO
class StrategyWriterHeb(StrategyWriter):
    def __init__(self,logger):
        super(StrategyWriterHeb,self).__init__(logger)
        self.writerlog = codecs.getwriter('utf - 8')(self.stream)
    def write_to_writer(self, data):
        #print "------ppppp---->writer got type :%s",type(data)
        self.logger.log(logging.DEBUG, "-------------->writer got type :%s", type(data))
        self.logger.log(logging.DEBUG, "writer got:%s", data)

        ret=self.writer.write(data)
        #self.writerlog.write(data)
        self.writerlog.write(data)
        self.writerlog.flush()
        self.logger.log(logging.DEBUG, "writer write:%s", self.stream.getvalue())
        #print "shoshan",self.stream.getvalue()
        self.stream.truncate(0)
        return ret



    def write(self, data):
        reversed = data[::-1]
        return self.write_to_writer(reversed)

    def getwriter(self,handle):
        self.handle = handle
        self.writer = codecs.getwriter('utf - 16')(handle)
        self.write_to_writer(
"""version=1
lefttoright=false
author=shoshan1
numeric=false

 """)
        return self
