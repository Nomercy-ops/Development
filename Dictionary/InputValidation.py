import re
from LogHandler import logger


class Validate:

    def getInteger():
        while True:
            try:
                number = int(input())
                return number
            except Exception:
                logger.error("not a proper input please try again")

    def getPositiveNumber():
        while True:
            try:
                numinput = int(input())
                # trying to check if the number is greater than 0
                if numinput > 0:
                    return numinput
                else:
                    logger.error("Enter a positive number")
            except:
                logger.erro("not a proper input please try again")
