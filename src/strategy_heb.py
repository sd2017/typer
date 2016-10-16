# -*- coding: utf-8 -*-
import codecs
import sys
import marshal

import logging
import logger
from kitchen.text.converters import getwriter, to_bytes, to_unicode
from kitchen.i18n import get_translation_object
from  strategy import Strategy
from StrategyWriterHeb import StrategyWriterHeb
class StrategyHeb(Strategy):
    def __init__(self,logger):
        super(StrategyHeb,self).__init__(logger)
        self.pairs=[u"חכ",u"לג",u"ךד",u"בש",u"נט",u"ןה",u"צק",u"יר",u"עם",u"נפ",u"ות",u"אמ",u"בס",u"טז"]
        #self.pairs = [ u"מו", u"אי",u"חכ", u"לג", u" ךד", u"בש", u"נט", u"ןה", u"צק", u"יר", u"עם", u"נפ", u"בס", u"טז"]

        UTF8Writer = codecs.getwriter('utf8')
        sys.stdout = UTF8Writer(sys.stdout)
        self.writer=StrategyWriterHeb(self.logger)

    def index(self, word):
        word_len = len(word)
        self.logger.log(logging.DEBUG,"word:%s", word)
        if word_len < 3:
            return None
        wordu3 = word[0:3]
        wordu=to_unicode(word,encoding='utf-8')

        wordb=to_bytes( wordu[0:3])
        self.logger.log(logging.DEBUG,wordb)
        word3=wordu[0:4]
        self.logger.log(logging.DEBUG, "i  wordu:%s", wordu)  #TODO clean
        self.logger.log(logging.DEBUG, "i  word3:%s", word3)
        self.logger.log(logging.DEBUG, "i wordu3:%s", word3)
        self.logger.log(logging.DEBUG, "i   word:%s", word)
        word3m = marshal.dumps(word3)
        return word3m

    def align(self, word):
        word_ret = word.strip(self.strip).strip(self.seperator)
        word_ret1 = to_unicode(word_ret)
        word_ret2=marshal.dumps(word_ret)
        return word_ret1
    def toSet(self,item):
        itemu=marshal.loads(item)
        seta=set(itemu)

        seta.discard(u'\n') #TODO WHY IS NOT STRIPPED
        seta.discard(u'u')
        return seta

    def levelToSet(self,level):
        setk=set()
        for i in xrange(0, level ):
            setk=setk.union(set(to_unicode(self.pairs[i])))
        self.logger.log(logging.DEBUG, "levelToSet:%s", setk)
        return setk

    def info(self):
        self.logger.log(logging.DEBUG, self.pairs)

if __name__=="__main__":
    logger=logger.Logger()
    tmp=StrategyHeb(logging)
    tmp.info()