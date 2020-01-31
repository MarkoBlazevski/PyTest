import logging
import inspect

def customLogger(file_level, console_level = None):
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG) # By default, log all messages

    if console_level != None:
        ch = logging.StreamHandler()
        ch.setLevel(console_level)
        ch_format = logging.Formatter('%(asctime)s - %(message)s')
        ch.setFormatter(ch_format)
        logger.addHandler(ch)

    fh = logging.FileHandler("{0}.log".format(loggerName))
    fh.setLevel(file_level)
    fh_format = logging.Formatter('%(asctime)s - %(name)s -  %(levelname)s: %(message)s',
                                  datefmt='%d/%m/%Y %I:%M:%S %p')

    fh.setFormatter(fh_format)
    logger.addHandler(fh)

    return logger