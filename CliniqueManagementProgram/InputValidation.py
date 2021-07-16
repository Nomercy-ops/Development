import re
from LoggerHandler import logger

class ValidateDetails:


    def validateName():
        """
    Description:
        This method is used for  validating name with regex pattern.

    Return:
        It retrun a valid name.
       
    """
        
        try:
            while True:
                name = input(" Enter Doctor or Patient Name : ")
                if re.match("^[A-Z]{1}[a-z]{4,}$", name):
                    return name
                else:
                    logger.error("Starting of name should be capital and length should be minimum of 4 characters ")
                    

        except ValueError:
            logger.error("Invalid input")

    
    def validateAvailablity():
        """
    Description:
        This method is used for  validating name with regex pattern.

    Return:
        It retrun a valid Time.
       
    """
        
        try:
            while True:
                availability = input("Availability(AM,PM OR BOTH: ")
                if re.match("^[0-9]{1,2}[A-Z]{2}$", availability):
                    return availability
                else:
                    logger.error(" Enter either 2AM 11AM or Pm")
                    

        except ValueError:
            logger.error("Invalid input")


    def validateSpeciality():
        """
    Description:
        This method is used for  validating speciality with regex pattern.

    Return:
        It retrun a valid name.
       
    """
        
        try:
            while True:
                speciality = input(" Enter Your Speciality: ")
                if re.match("[A-Za-z]{8,}$", speciality):
                    return speciality
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
                    if re.match("^[7-9]{1}[0-9]{9}$", mobileNumber):
                        return mobileNumber
                    else:
                        logger.error("Mobile number should be in this format (8235465768) and start with 7 8 or 9 ")
                        
        except ValueError:

            logger.error("Invalid input")

  

    
    def validateAge():
        """
    Description:
        This method is used for validating Age with regex pattern.

    Return:
        It return a valid mobile number.
       
    """
        try:
            while True:
                    age = input(" Enter Your Age : ")
                    if re.match("^[1-9]{1}[0-9]{1}$", age):
                        return age
                    else:
                        logger.error("Age length should not be more than 2")
                        
        except ValueError:

            logger.error("Invalid input")

    
    def validateId():
        """
    Description:
        This method is used for validating Age with regex pattern.

    Return:
        It retrun a valid Id .
       
    """
        try:
            while True:
                    id = input(" Enter Your Id : ")
                    if re.match("^[0-9]{2,4}$", id):
                        return id
                    else:
                        print("Id length should be less than 4 ")
                        
        except ValueError:

            logger.error("Invalid input")






            

    
    