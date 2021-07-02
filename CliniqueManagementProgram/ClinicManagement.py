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

if __name__ == "__main__":

    try:

        print(" Welcome to Clinic Management System ")

        while True:
            # reading json files
            
            
            
            print("1.Add Doctor")
            print("2.Add Patients")
            print("3.Print Doctor")
            print("4.Print Patients")
            print("5.Exit")

        
       
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

    
            else:
                exit()

    except ValueError:
        logger.error("Invalid choice")
    
    except Exception as e:
        logger.error(e)
