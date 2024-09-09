import inspect
import logging


def custom_logger(loglevel=logging.DEBUG):
    # Gets the name of the class/method from where it is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    # By default, log all the messages
    logger.setLevel(logging.INFO)

    fileHandler = logging.FileHandler("automation.log".format(loggerName), mode='a')  # here 'a' means Append
    fileHandler.setLevel(loglevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  datefmt='%m/%d/%Y %H:%M:%S %p')
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)

    return logger
