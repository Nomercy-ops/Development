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
    def getMObileNumber(self):
        return self.__mobileNumber

    def setMobileNumber(self, mobilenumber):
        self.__mobileNumber = mobilenumber

    def toString(self):
        jsonFile = {"Id": self.getPatientId(), "Name": self.getPatientName(
        ), "Age": self.getAge(), "Mobile": self.getMObileNumber(),"DoctorId":""}
        return jsonFile

    def readfile(self):
        try:

            with open('patients'+'.json', 'r') as file:
                self.list = json.load(file)

        except FileNotFoundError:
            logger.error('Invalid file name')


    def writeFile(self):
        try:
            with open('patients' + '.json', 'w+') as file:
                json.dump(self.list, file, indent=2)
                logger.info("file successfully saved...")
        
        except Exception as e:
            logger.error(e)

        finally:
                file.close()


    def addPatient(self):
        print("Enter the Patients details here")

        self.patientId = input("Enter Patient Id: ")
        self.setPatientId(self.patientId)

        self.patientName = input("Enter Patient Name: ")
        self.setPatientName(self.patientName)

        self.age = input("Enter Patient Age: ")
        self.setAge(self.age)

        self.mobileNumber = input("Enter Patient mobileNUmber: ")
        self.setMobileNumber(self.mobileNumber)

        patientDetails = self.list
        patientDetails.append(self.toString())
        self.writeFile()

patient = Patient()


