
import json
from LoggerHandler import logger


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
        try:

            with open('doctors'+'.json', 'r') as file:
                self.list = json.load(file)

        except FileNotFoundError:
            logger.error('Invalid file name')


    def writeFile(self):
        try:
            with open('doctors' + '.json', 'w+') as file:
                json.dump(self.list, file, indent=2)
                logger.info("file successfully saved...")
        
        except Exception as e:
            logger.error(e)

        finally:
                file.close()
            

    def addDoctor(self):
        print("Enter the doctor details here")

        addDoctor = {}

        self.doctorId = input("Enter doctor Id: ")
        self.setDoctorId(self.doctorId)
        addDoctor['id'] = self.getDoctorId()

        self.doctorName = input("Enter Doctor Name: ")
        self.setDoctorName(self.doctorName)
        addDoctor['name'] = self.getDoctorName()

        self.availability = input("Enter doctor Availability(AM,PM OR BOTH): ")
        self.setAvailability(self.availability)
        addDoctor['availability'] = self.getAvailability()

        self.specialist = input("Enter Doctor speciality: ")
        self.setSpecialist(self.specialist)
        addDoctor['speciality'] = self.getSpecialist()

        self.list['doctorlist'].append(addDoctor)
        self.writeFile()

    def printDoctorList(self):
        with open('doctors' + '.json', 'r') as file:
            self.list = json.load(file)
            logger.info(self.list)
        
doctor = Doctor()
