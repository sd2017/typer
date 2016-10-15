# -*- coding: utf-8 -*-
import logging
import sys

def Loggerf():

    if (None==Loggerf.global_logger):
        print "initializing logger"
        loggeri=Logger()
        Loggerf.global_logger=logging.getLogger('typer')
    return Loggerf.global_logger
Loggerf.global_logger = None
class Logger():
    def __init__(self):
        root_logger = logging.getLogger('typer')
        root_logger.setLevel(logging.INFO)  # or whatever
        handler = logging.StreamHandler()  # or whatever

        #handler = logging.FileHandler('test.log', 'w', 'utf-8')  # or whatever
        handler.setFormatter = logging.Formatter('%(name)s %(message)s')  # or whatever
        if (None==Loggerf.global_logger):
          root_logger.addHandler(handler)


        # formatter = logging.Formatter("%(message)s")
        # new_formatter ={
        #     'simple': {
        #         'format': u'%(asctime)-s %(levelname)s [%(name)s]: %(message)s',
        #         'datefmt': '%Y-%m-%d %H:%M:%S',
        #     }
        #  formatter.
        # }
        #
        # logging._defaultFormatter = logging.Formatter(u"%(message)s")