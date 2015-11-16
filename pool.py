#!/usr/bin/env python
#coding=utf-8


from multiprocessing.dummy import Pool
from settings import THREAD_NUMBER
from settings import logger


def singleton(cls, *args, **kw):    
    instances = {}    
    def _singleton():    
        if cls not in instances:    
            instances[cls] = cls(*args, **kw)    
        return instances[cls]    
    return _singleton   

@singleton
class ScannerPool:
   # @classmethod
   # def getPool(cls):
   #     if "pool" not in cls.__dict__ or cls.pool is None:
   #         logger.info("Threads pool created with %d threads" % THREAD_NUMBER)
   #         cls.pool = Pool(THREAD_NUMBER)
    #        return cls.pool

    def __init__(self):
        self.pool = Pool(THREAD_NUMBER)


    def map(self, *args, **kwargs):
        return self.pool.imap_unordered(*args, **kwargs)
