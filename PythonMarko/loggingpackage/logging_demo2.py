import logging
import loggingpackage.custom_logger as cl

class LoggingDemo2():

    log = cl.customLogger(logging.DEBUG)

    def methot1(self):
        self.log.debug("debug message")
        self.log.info("info message")
        self.log.warning("warning message")
        self.log.error("error message")
        self.log.critical("critical message")

    def method2(self):
        m2Log = cl.customLogger(logging.INFO)
        m2Log.debug("debug message")
        m2Log.info("info message")
        m2Log.warning("warning message")
        m2Log.error("error message")
        m2Log.critical("critical message")

    def method3(self):
        self.log.debug("debug message")
        self.log.info("info message")
        self.log.warning("warning message")
        self.log.error("error message")
        self.log.critical("critical message")

demo = LoggingDemo2()
demo.methot1()
demo.method2()
demo.method3()