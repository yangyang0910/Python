# -*- coding:utf-8 -*-
# AUTHER   @ Alvin

import logging

logging.basicConfig(
    filename="errorinfo.log",
    level=logging.DEBUG,
    format='%(asctime)s %(message)s %(levelno)s %(levelname)s %(pathname)s %(filename)s %(module)s %(funcName)s %(lineno)d %(message)s',
    datefmt='%Y-%d-%m %I:%M:%S %p'
)

logging.warning("")
logging.info("")
logging.debug("")
logging.error("")
logging.critical("")
