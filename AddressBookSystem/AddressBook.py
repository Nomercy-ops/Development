import json
from LoggerFormat import logger
from UserDetailsValidation import ValidateDetails


class AddressBookManage:
   

    def __init__(self):
        self.list = []
                 

    def openFile(self):
        """
    Description:
        This method is used for opening and loading stored details from a json file.
    Parameter:
        It takes self as a parameter and load all the data from json file to a list.
       
    """

        try:

            with open('address'+'.json', 'r') as file:
                self.list = json.load(file)

        except FileNotFoundError:
            logger.error('Invalid file name')
            

    def addDetails(self):
        """
    Description:
        This method is used for adding a address book details in address book.
        it creates a dictionary and add details into it and then append them to a list.
    Parameter:
        It takes self as a parameter and append details into list.
       
    """
        addNew = {}
        id = ValidateDetails.getId()
        addNew['id'] = id
        firstName = ValidateDetails.validateName()
        addNew['firstname'] = firstName
        lastName = ValidateDetails.validateName()
        addNew['lastname'] = lastName
        mobileNumber = ValidateDetails.validateNumber()
        addNew['mobilenumber'] = mobileNumber
        address = ValidateDetails.validateAddress()
        addNew['address'] = address
        zipcode = ValidateDetails.validateZipcode()
        addNew['zipcode'] = zipcode
        city = ValidateDetails.validateCity()
        addNew['city'] = city
        state = ValidateDetails.validateState()
        addNew['state'] = state
        self.list['data'].append(addNew)
        self.saveDetails()

    def saveDetails(self):
        """
    Description:
        This method is writing or storing address book details from list into json file
    Parameter:
        It takes self as a parameter to get addressbook details stored inside list and
        using json dump it writes those details inside json file.
       
    """
        try:
            with open('address' + '.json', 'w+') as file:
                json.dump(self.list, file, indent=2)
                logger.info("file successfully saved...")
        
        except Exception as e:
            logger.error(e)

        finally:
                file.close()
            

    def updateDetails(self):
        """
    Description:
        This method is used for update addressbook details from the json file

    Parameter:
        It takes self as a parameter to get addressbook details stored inside list and
        update the details and save them into json file.
       
    """
        try:
            
            flag = updateDetails = False
            if len(self.list['data']) >= 1:
                idNumber = input("Enter Your Unique id : ")
                for i in range(len(self.list['data'])):
                    if (self.list['data'][i]['id'] == idNumber):
                        flag = True
                        if flag:
                            option = int(
                            input(" Select Any One Option to update your Profile\n 1 First Name \n 2 Last Name \n 3 Mobile Number\n 4 Address \n 5 Zipcode \n 6 city \n 7 state \n "))

                            if option == 1:
                                firstName = ValidateDetails.validateName()
                                self.list['data'][i]['firstname'] = firstName
                                self.saveDetails()
                                updateDetails = True

                            elif option == 2:
                                lastName = ValidateDetails.validateName()
                                self.list['data'][i]['lastname'] = lastName
                                self.saveDetails()
                                updateDetails = True

                            elif option == 3:
                                mobileNumber = ValidateDetails.validateNumber()
                                self.list['data'][i]['mobilenumber'] = mobileNumber
                                self.saveDetails()
                                updateDetails = True

                            elif option == 4:
                                address = ValidateDetails.validateAddress()
                                self.list['data'][i]['address'] = address
                                self.saveDetails()
                                updateDetails = True

                            elif option == 5:
                                zipcode = ValidateDetails.validateZipcode()
                                self.list['data'][i]['zipcode'] = zipcode
                                self.saveDetails()
                                updateDetails = True

                            elif option == 6:
                                city = ValidateDetails.validateCity()
                                self.list['data'][i]['city'] = city
                                self.saveDetails()
                                updateDetails = True

                            elif option == 7:
                                state = ValidateDetails.validateState()
                                self.list['data'][i]['state'] = state
                                self.saveDetails()
                                updateDetails = True

                            else:
                                print("Invalid Option")
                                updateDetails = False
                                self.updateDetails()

        except ValueError:
                        logger.error("Enter a valid option")
                        updateDetails = False
                        self.updateDetails()

        except Exception as e:
            logger.error(e)
            self.updateDetails()


    def removeDetails(self):
        """
    Description:
        This method is used for deleting address book details from the json file.

    Parameter:
        It takes self as a parameter to get addressbook details stored inside list and
        delete the details and saved the json file.
       
    """ 
        try:
            if len(self.list['data']) >= 1:
                idNumber = input("Enter Your Unique id : ")
                for i in range(len(self.list['data'])):
                    if ((self.list['data'][i]['id']) == idNumber): 
                        logger.info(" Data Removed Successfully ")
                        del self.list['data'][i]
                        self.saveDetails()
                        return
                    
        except Exception as e:
            logger.error(e)


    def displayDetails(self):
        """
    Description:
        This method is used for displaying addressbook details from a json file

    Parameter:
        It takes self as a parameter to get addressbook details stored inside list and
        display all the stored details.
       
    """
        with open('address' + '.json', 'r') as file:
            self.list = json.load(file)
            logger.info(self.list)
           
            
          
            
