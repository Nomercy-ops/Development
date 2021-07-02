
import json
from LoggerHandler import logger
from InputValidation import ValidateDetails


class Doctor():
     # class level private variables
    __doctorId = None
    __doctorName = None
    __availability = None
    __specialist = None


    def __init__(self):
        
        self.list = []

     # getter and setter method for doctor Id
    def getDoctorId(self):
        return self.__doctorId

    def setDoctorId(self, doctorId):
        self.__doctorId = doctorId

    # getter and setter method for doctor Name
    def getDoctorName(self):
        return self.__doctorName

    def setDoctorName(self, doctorName):
        self.__doctorName = doctorName

    # getter and setter method for doctor availability

    def getAvailability(self):
        return self.__availability

    def setAvailability(self, availability):
        self.__availability = availability

    # getter and setter method for doctor speciality
    def getSpecialist(self):
        return self.__specialist

    def setSpecialist(self, spec):
        self.__specialist = spec

   
    def readfile(self):
        """
    Description:
        This method is used for opening and loading stored details from a json file.
    Parameter:
        It takes self as a parameter and load all the data from json file to a list.
       
    """
        try:

            with open('doctors'+'.json', 'r') as file:
                self.list = json.load(file)

        except FileNotFoundError:
            logger.error('Invalid file name')
            


    def writeFile(self):
        """
    Description:
        This method is used for adding a doctor details in json file.
        it creates a dictionary and add details into it and then append them to a list.
    Parameter:
        It takes self as a parameter and append details into list.
       
    """
        try:
            with open('doctors' + '.json', 'w+') as file:
                json.dump(self.list, file, indent=2)
                logger.info("file successfully saved...")
        
        except Exception as e:
            logger.error(e)

        finally:
                file.close()
            

    def addDoctor(self):
        """
    Description:
        This method is used for adding a doctor details.
        it creates a dictionary and add details into it and then append them to a list.
    Parameter:
        It takes self as a parameter and append details into list.
       
    """
        print("Enter the doctor details here")

        addDoctor = {}

        self.doctorId = ValidateDetails.validateId()
        self.setDoctorId(self.doctorId)
        addDoctor['id'] = self.getDoctorId()

        self.doctorName = ValidateDetails.validateName()
        self.setDoctorName(self.doctorName)
        addDoctor['name'] = self.getDoctorName()

        self.availability = ValidateDetails.validateAvailablity()
        self.setAvailability(self.availability)
        addDoctor['availability'] = self.getAvailability()

        self.specialist = ValidateDetails.validateSpeciality()
        self.setSpecialist(self.specialist)
        addDoctor['specialist'] = self.getSpecialist()

        self.list['doctorlist'].append(addDoctor)
        self.writeFile()

    def printDoctorList(self):
        with open('doctors' + '.json', 'r') as file:
            self.list = json.load(file)
            logger.info(self.list)


        
doctor = Doctor()
