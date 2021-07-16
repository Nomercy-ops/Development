"""
@Author: Rikesh Chhetri
@Date: 2021-07-02 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-02 07:03:30
@Title : Program Aim is to manage a list of Doctors associated with the Clinique.
"""

from Appointment import TakeAppoinment
from DoctorModel import doctor
from PatientModel import patient
from LoggerHandler import logger

if __name__ == "__main__":

    try:

        print(" Welcome to Clinic Management System ")

        while True:

            print("1.Add Doctor")
            print("2.Add Patients")
            print("3.Print Doctor")
            print("4.Print Patients")
            print("5.Take Appointment")
            print("6.Search Doctor BY Id")
            print("7.Search Patient BY Id")
            print("8.Search Doctor BY Name")
            print("9.Search Patient BY Name")
            print("10.Exit")
        
       
            choice = input("Enter your choice: ")

            if choice == '1':
                doctor.readfile()
                doctor.addDoctor()
        
    
            elif choice == '2': 
                patient.readfile()
                patient.addPatient()

            elif choice == '3':
                doctor.printDoctorList()

            elif choice == '4':
                patient.printPatientList()

            elif choice == '5':
                TakeAppoinment.getAppointment()
            
            elif choice == '6':
                doctor.readfile()
                doctor.searchDoctorById()

            elif choice == '7':
                patient.readfile()
                patient.searchPatientById()
            
            elif choice == '8':
                doctor.readfile()
                doctor.searchDoctorByName()
            
            elif choice == '9':
                patient.readfile()
                patient.searchPatientByName()

    
            else:
                exit()

    except ValueError:
        logger.error("Invalid choice")
    
    except Exception as e:
        logger.error(e)
