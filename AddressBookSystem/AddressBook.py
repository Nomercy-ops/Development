import json
import logging

# logging basic config method and saving log files
logging.basicConfig(filename='addressbook.log', level=logging.INFO,
                    format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')
logging.basicConfig(filename='addressbook.log', level=logging.ERROR,
                    format='%(asctime)s:%(funcName)s:%(levelname)s:%(lineno)d')


class AddressBookManage:

    def __init__(self):
        self.list = []


    def createFile(self):
        """
    Description:
        This method is used for creating a json file for storing addressbook details.
    Parameter:
        It takes self as a parameter  to create items of list inside json file.
       
    """
        try:
            self.list = {'data': []}
            with open('rikesh'+'.json', 'a+') as file:
                json.dump(self.list, file, indent=2)
                logging.info('File Successfully Created..')
        except Exception as e:
            logging.error(e)
        
        finally:
                file.close()
            

    def openFile(self):
        """
    Description:
        This method is used for opening and loading stored details from a json file.
    Parameter:
        It takes self as a parameter and load all the data from json file to a list.
       
    """

        try:

            with open('rikesh'+'.json', 'r') as file:
                self.list = json.load(file)

        except FileNotFoundError:
            logging.error('Invalid file name')

    def addDetails(self):
        """
    Description:
        This method is used for adding a address book details in address book.
        it creates a dictionary and add details into it and then append them to a list.
    Parameter:
        It takes self as a parameter and append details into list.
       
    """
        addNew = {}
        firstName = input("Enter your first name: ")
        addNew['firstname'] = firstName
        lastName = input("Enter your last name: ")
        addNew['lastname'] = lastName
        mobileNumber = input("Enter your phone number: ")
        addNew['mobilenumber'] = mobileNumber
        address = input("Enter your address ")
        addNew['address'] = address
        zipcode = input("Enter your zipcode: ")
        addNew['zipcode'] = zipcode
        city = input("Enter your city name: ")
        addNew['city'] = city
        state = input("Enter your state name: ")
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
            with open('rikesh' + '.json', 'w+') as file:
                json.dump(self.list, file, indent=2)
                logging.info("file successfully saved...")
        
        except Exception as e:
            logging.error(e)

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
                fName = input("Enter the First Name ")
                lName = input("Enter the Last Name ")
                for i in range(len(self.list['data'])):
                    if (self.list['data'][i]['firstname'] == fName) and (self.list['data'][i]['lastname'] == lName):
                        flag = True
                        if flag:
                            option = int(
                            input(" Select AnyOne Option to update your Profile\n 1 First Name \n 2 Last Name \n 3 Mobile Number\n 4 Address \n 5 Zipcode \n 6 city \n 7 state \n "))

                            if option == 1:
                                firstName = int(
                                    input("Enter new First Name : "))
                                self.list['data'][i]['firstname'] = firstName
                                self.saveDetails()
                                updateDetails = True

                            elif option == 2:
                                lastName = int(input("Enter new Last Name : "))
                                self.list['data'][i]['lastname'] = lastName
                                self.saveDetails()
                                updateDetails = True

                            elif option == 3:
                                mobileNumber = int(
                                    input("Enter new Mobile number : "))
                                self.list['data'][i]['mobilenumber'] = mobileNumber
                                self.saveDetails()
                                updateDetails = True

                            elif option == 4:
                                address = input("Enter your new Address : ")
                                self.list['data'][i]['address'] = address
                                self.saveDetails()
                                updateDetails = True

                            elif option == 5:
                                zipcode = int(input("Enter new zipcode : "))
                                self.list['data'][i]['zipcode'] = zipcode
                                self.saveDetails()
                                updateDetails = True

                            elif option == 6:
                                city = input("Enter new city name : ")
                                self.list['data'][i]['city'] = city
                                self.saveDetails()
                                updateDetails = True

                            elif option == 7:
                                state = input("Enter new state name : ")
                                self.list['data'][i]['state'] = state
                                self.saveDetails()
                                updateDetails = True

                            else:
                                print("Invalid Option")
                                updateDetails = False
                                self.updateDetails()

        except ValueError:
                        logging.error("Enter a valid option")
                        updateDetails = False
                        self.updateDetails()

        except Exception as e:
            logging.error(e)
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
                firstName = input("Enter the First Name ")
                lastName = input("Enter the Last Name ")
                for i in range(len(self.list['data'])):
                    if ((self.list['data'][i]['firstname']) == firstName and (self.list['data'][i]['lastname']) == lastName):
                        logging.info(" Data Removed Successfully ")
                        del self.list['data'][i]
                        self.saveDetails()
                        return
                    
        except Exception as e:
            logging.error(e)


    def displayDetails(self):
        """
    Description:
        This method is used for displaying addressbook details from a json file

    Parameter:
        It takes self as a parameter to get addressbook details stored inside list and
        display all the stored details.
       
    """
        with open('rikesh' + '.json', 'r') as file:
            self.list = json.load(file)
            logging.info(self.list)
