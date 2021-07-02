from os import name
from InputValidation import ValidateDetails
import json
from LoggerHandler import logger

class Patient():

    # class level private variables
    __patientId = None
    __patientName = None
    __age = None
    __mobileNumber = None

    def __init__(self):
       self.list = []

    # getter and setter method for doctor Id
    def getPatientId(self):
        return self.__patientId

    def setPatientId(self, patientId):
        self.__patientId = patientId

    # getter and setter method for doctor Name
    def getPatientName(self):
        return self.__patientName

    def setPatientName(self, patientName):
        self.__patientName = patientName

    # getter and setter method for doctor availability

    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age

    # getter and setter method for doctor speciality
    def getMobileNumber(self):
        return self.__mobileNumber

    def setMobileNumber(self, mobileNumber):
        self.__mobileNumber = mobileNumber


    def readfile(self):
        """
    Description:
        This method is used for opening and loading stored details from a json file.
    Parameter:
        It takes self as a parameter and load all the data from json file to a list.
       
    """
        try:

            with open('patients'+'.json', 'r') as file:
                self.list = json.load(file)

        except FileNotFoundError:
            logger.error('Invalid file name')


    def writeFile(self):
        """
    Description:
        This method is used for adding a patient details in json file.
        it creates a dictionary and add details into it and then append them to a list.
    Parameter:
        It takes self as a parameter and append details into list.
       
    """
        try:
            with open('patients' + '.json', 'w+') as file:
                json.dump(self.list, file, indent=2)
                logger.info("file successfully saved...")
        
        except Exception as e:
            logger.error(e)

        finally:
                file.close()


    def addPatient(self):
        """
    Description:
        This method is used for adding a Patient details.
        it creates a dictionary and add details into it and then append them to a list.
    Parameter:
        It takes self as a parameter and append details into list.
       
    """
        print("Enter the Patients details here")

        addPatient = {}

        self.patientId = ValidateDetails.validateId()
        self.setPatientId(self.patientId)
        addPatient['id'] = self.getPatientId()

        self.patientName = ValidateDetails.validateName()
        self.setPatientName(self.patientName)
        addPatient['name'] = self.getPatientName()

        self.age = ValidateDetails.validateAge()
        self.setAge(self.age)
        addPatient['age'] = self.getAge()

        self.mobileNumber = ValidateDetails.validateNumber()
        self.setMobileNumber(self.mobileNumber)
        addPatient['number'] = self.getMobileNumber()

        self.list['patientlist'].append(addPatient)
        self.writeFile()

    def printPatientList(self):
        """
    Description:
        This method is used for displaying all the list of patients
       
    """
        with open('patients' + '.json', 'r') as file:
            self.list = json.load(file)
            logger.info(self.list)

    
    def searchPatientById(self):
        """
    Description:
        This method is used to find the Patient by id
       
    """
        try:
                idNumber = ValidateDetails.validateId()
                for i in range(len(self.list['patientlist'])):
                    if ((self.list['patientlist'][i]['id']) == idNumber): 
                        logger.info(" Patient is Available")
                        break
                    else:
                        logger.info(" Patient is currently Not Available")
                    
        except Exception as e:
            logger.error(e)

    
    def searchPatientByName(self):
        """
    Description:
        This method is used to find the Patient by name
       
    """
        try:
                name = ValidateDetails.validateName()
                for i in range(len(self.list['patientlist'])):
                    if ((self.list['patientlist'][i]['name']) == name): 
                        logger.info(" Patient is Available")
                        break
                    else:
                        logger.info(" Patient is currently Not Available")
                    
        except Exception as e:
            logger.error(e)



patient = Patient()


