"""
@Author: Rikesh Chhetri
@Date: 2021-07-02 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-02 07:03:30
@Title : Program Aim is to manage a list of Doctors associated with the Clinique.
"""

from DoctorModel import doctor
from PatientModel import patient
from LoggerHandler import logger

try:

    print(" Welcome to Clinic Management System ")

    while True:
        # choice input

        print("1.Add Doctor")
        print("2.Add Patients")
        print("3.Print Doctor")
        print("4.Print Patients")
        print("5.Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            doctor.addDoctor()
        
    
        elif choice == '2':
            patient.addPatient()
    

        else:
            exit()

except ValueError:
    logger.error("Invalid choice")
    
except Exception as e:
    logger.error(e)
