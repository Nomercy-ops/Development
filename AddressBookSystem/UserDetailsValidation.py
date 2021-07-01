from LoggerFormat import logger
import re
import random
import json

class ValidateDetails:


    def validateName():
        """
    Description:
        This method is used for  validating name with regex pattern.

    Return:
        It retrun a valid first name and last name.
       
    """
        
        try:
            while True:
                name = input(" Enter Your First Name : ")
                if re.match("^[A-Z]{1}[a-z]{4,}$", name):
                    return name
                else:
                    logger.error("Starting of name should be capital and length should be minimum of 4 characters ")
                    

        except ValueError:
            logger.error("Invalid input")

    def validateNumber():
        """
    Description:
        This method is used for validating mobile number with regex pattern.

    Return:
        It retrun a valid mobile number.
       
    """
        try:
            while True:
                    mobileNumber = input(" Enter Your Mobile Number : ")
                    if re.match("[0-9]{10}$", mobileNumber):
                        return mobileNumber
                    else:
                        logger.error("Mobile number should be in this format (+91-8235465768) ")
                        
        except ValueError:

            logger.error("Invalid input")


    def validateZipcode():
        """
    Description:
        This method is used for  validating zipcode with regex pattern.

    Return:
        It retrun a valid zipcode.
       
    """
        try:
            while True:
                    zipcode = input(" Enter Your zipcode : ")
                    if re.match("[0-9]{6}$", zipcode):
                        return zipcode
                    else:
                        logger.error("Enter a valid zipcode")
                        
        except ValueError:
            print("Invalid input")

    
    def validateAddress():
        """
    Description:
        This method is used for  validating address with regex pattern.

    Return:
        It retrun a valid address.
       
    """
        try:
            while True:
                    addressName = input(" Enter Your Address : ")
                    if re.match("[a-zA-Z0-9]*$", addressName):
                        return addressName
                    else:
                        logger.error("Enter a Valid address Name ")
                        
        except ValueError:
            logger.error("Invalid input")

    def validateCity():
        """
    Description:
        This method is used for  validating city name with regex pattern.

    Return:
        It retrun a valid city name.
       
    """
        try:
            while True:
                    cityName = input(" Enter Your City Name : ")
                    if re.match("[a-zA-Z]*$", cityName):
                        return cityName
                    else:
                        logger.error("Enter valid City name")
                        
        except ValueError:

            logger.error("Invalid input")

    
    def validateState():
        """
    Description:
        This method is used for validating state name with regex pattern.

    Return:
        It retrun a valid state name.
       
    """
        try:
            while True:
                    stateName = input(" Enter Your State name : ")
                    if re.match("[a-zA-Z]*$", stateName):
                        return stateName
                    else:
                        logger.error("Enter valid state name")
                        
        except ValueError:

            logger.error("Invalid input")

    
    def getId():
        try:
            while True:
                    id = input(" Enter unique id : ")
                    if re.match("^[0-9]{2,3}$", id):
                        return id
                    else:
                        logger.error("Enter valid id ")
                        
        except ValueError:
            logger.error("Invalid input")



        