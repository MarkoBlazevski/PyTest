"""
Logger Demo
"""
import logging
import logging.config

class LogggerDemoConf():

    def testLog(self):
        # create logger
        logging.config.fileConfig("logging.conf")
        logger = logging.getLogger(LogggerDemoConf.__name__)

        # logging messags
        logger.debug("debug message")
        logger.info("info message")
        logger.warning("warning message")
        logger.error("error message")
        logger.critical("critical message")

demo = LogggerDemoConf()
demo.testLog()