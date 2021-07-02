from LoggerHandler import logger
import re

class ValidateDetails:

    def validateName():
        """
    Description:
        This method is used for  validating name with regex pattern.

    Return:
        It retrun a valid name

    """

        try:
            while True:
                name = input("name the stock you want to add : ")
                if re.match("^[A-Z]{1}[a-z]{5,}$", name):
                    return name
                else:
                    logger.error(
                        "Starting of name should be capital and length should be minimum of 4 characters ")

        except ValueError:
            logger.error("Invalid input")
        except Exception as e:
            logger.error(e)

 
               