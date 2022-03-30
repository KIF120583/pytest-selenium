import logging
import logging.handlers

class getlogger:

    def __init__(self , logname , loggername = __name__):

        # create logger
        print(loggername)
        self.logger = logging.getLogger(loggername)
        time_rotating_handler = logging.handlers.TimedRotatingFileHandler(logname)
        self.logger.setLevel(logging.DEBUG)

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # add formatter to ch
        ch.setFormatter(formatter)
        time_rotating_handler.setFormatter(formatter)

        # add ch to logger
        self.logger.addHandler(ch)
        self.logger.addHandler(time_rotating_handler)

    def debug(self , message):
        self.logger.debug(message)
    def info(self , message):
        self.logger.info(message)
    def warning(self , message):
        self.logger.warning(message)
    def error(self , message):
        self.logger.error(message)
    def critical(self , message):
        self.logger.critical(message)

if __name__ == "__main__":
    mylogger = getlogger(logname="test.log")
    mylogger.debug('debug message')
    mylogger.debug('debug message')
    mylogger.info('info message')
    mylogger.warning('warn message')
    mylogger.error('error message')
    mylogger.critical('critical message')
