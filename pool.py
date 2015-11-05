#!/usr/bin/env python


from multiprocessing.dummy import Pool
from settings import THREAD_NUMBER
from settings import logger



class ScannerPool:
    @classmethod
    def getPool(cls):
        if "pool" not in cls.__dict__ or cls.pool is None:
            logger.info("Threads pool created with %d threads" % THREAD_NUMBER)
            cls.pool = Pool(THREAD_NUMBER)
            return cls.pool

