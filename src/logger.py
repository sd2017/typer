# -*- coding: utf-8 -*-
import logging
class Logger:
    def __init__(self):
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)  # or whatever
        handler = logging.FileHandler('test.log', 'w', 'utf-8')  # or whatever
        handler.setFormatter = logging.Formatter('%(name)s %(message)s')  # or whatever
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