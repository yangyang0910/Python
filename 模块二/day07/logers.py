# -*- coding:utf-8 -*-
# AUTHER   @ Alvin

import logging
# Logger = logging.getLogger("web")
Loddings = logging.getLogger("Loggers")
# 指定最低的日志级别，低于lel的级别将被忽略。debug是最低的内置级别，critical为最高
Loddings.setLevel(logging.INFO)
# 生成文件hdler
hdlr = logging.StreamHandler()
filt = logging.FileHandler("Loggers.log")
hdlr.setLevel(logging.ERROR)
filt.setLevel(logging.NOTSET)
#添加或删除指定的filter
Loddings.addHandler(filt)
# 生成hdler对象
# Logger.removeFilter(filt)
# 增加或删除指定的handler
Loddings.addHandler(hdlr)
# Logger.removeHandler(hdlr)
# 打印到文件日志
file_formater = logging.Formatter("%(asctime)s %(message)s %(levelno)s %(levelname)s %(pathname)s %(filename)s %(module)s %(funcName)s %(lineno)d %(message)s")
# 打印到屏幕日志
# 打印到屏幕日志
console_formater = logging.Formatter("%(asctime)s %(message)s %(levelno)s %(filename)s")

filt.setFormatter(file_formater)
hdlr.setFormatter(console_formater)

Loddings.debug("debug")
Loddings.warning("warning")
Loddings.info("info")
Loddings.critical("critical")
Loddings.error("error")





