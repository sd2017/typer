import codecs
import logging
import logger
from StringIO import StringIO
class StrategyWriter(object):
    def __init__(self,logger):
        self.logger=logger
        self.handle = None
        self.writer = None
        self.stream = StringIO()
        self.writerlog = self.stream
        self.writerlog = codecs.getwriter('utf - 8')(self.stream)

    def write_to_writer(self, data):
        # print "------ppppp---->writer got type :%s",type(data)
        self.logger.log(logging.DEBUG, "-------------->writer got type :%s", type(data))
        self.logger.log(logging.DEBUG, "writer got:%s", data)

        ret = self.writer.write(data)
        # self.writerlog.write(data)
        self.writerlog.write(data)
        self.writerlog.flush()
        self.logger.log(logging.DEBUG, "writer write:%s", self.stream.getvalue())
        # print "shoshan",self.stream.getvalue()
        self.stream.truncate(0)
        return ret

    def write(self, data):
        return self.write_to_writer(data)

    def getwriter(self, handle):
        self.handle = handle
        self.writer = codecs.getwriter('utf - 16')(handle)
        self.write_to_writer(
"""version=1
lefttoright=true
author=shoshan1
numeric=false

 """)
        return self
