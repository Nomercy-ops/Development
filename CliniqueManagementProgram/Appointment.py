from LoggerHandler import logger
from InputValidation import ValidateDetails
import json


class TakeAppoinment:

    def getAppointment():
        """
    Description:
        This method is used for getting appointment from the doctor.
        Here we Add the patient info and doctor details for the appointment.
       
    """
        try:
            getDoctor = []
            with open('doctors'+'.json', 'r') as file:
                getDoctor = json.load(file)
            doctors = getDoctor["doctorlist"]
            for i in range(len(doctors)):
                name = doctors[i]['name']
                speciality = doctors[i]['specialist']
                available = doctors[i]['availability']
                print(name, '  ', speciality, '  ', available)
                print()


            
            doctorName = ValidateDetails.validateName()
            time = ValidateDetails.validateAvailablity()
            #reading appoinment file and adding to appoinment.
            #getting doctor details
            with open('appointments'+'.json', 'r') as file:
                appointmentDetails = json.load(file)
            appointmentList = appointmentDetails[doctorName]
            print("Appointment list is ", appointmentList)
           
            
            # checking appointment list whether it contained more than 5 appointment or not.
            # if not then add appointment with that doctor.
            if len(appointmentList) <= 5:
                for i in range(len(doctors)):
                    if doctors[i]["name"] == doctorName:
                        if time.upper() == doctors[i]["availability"]:
                            logger.info("Doctor is Available..!! Please Enter the patient details:")
                            
                            # Taking User Input If Doctor is available 
                            name = ValidateDetails.validateName()
                            id = ValidateDetails.validateId()
                            age = ValidateDetails.validateAge()
                            mobileNumber = ValidateDetails.validateNumber()

                            with open('appointments.json', 'r')as f:
                                file = f.read()
                                appointmentfile = json.loads(file)
                            newAppointmentDic = {
                                "patientName": name, "Id": id, "patientAge": age, "mobileNumber": mobileNumber, "time": time}
                            with open('appointments.json', 'a+') as files:
                                appointmentfile[doctorName].append(newAppointmentDic)
                                files.write(json.dumps(appointmentfile, indent=2))
                            logger.info("Your appointment Has Been fixed. Thank You !")
                        else:
                            logger.info("This Doctor is not Available !! ")

        except FileNotFoundError:
            logger.error('Invalid file name')
        
        finally:
            file.close()
