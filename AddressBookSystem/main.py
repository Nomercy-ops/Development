"""
@Author: Rikesh Chhetri
@Date: 2021-07-01 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-01 10:03:30
@Title : Program Aim perform CRUD operations on address book
"""

from AddressBook import AddressBookManage
import logging

logging.basicConfig(filename='addressbook.log', level=logging.ERROR,
                    format='%(asctime)s:%(funcName)s:%(levelname)s:%(lineno)d')

if __name__ == "__main__":
    
    try:

        while True:
            address = AddressBookManage()  # creating address object to get access attributes of addessbook manage.

            def addDetails():
                """
    Description:
        This function is used for calling add method of Address book manage class
       
    """
                address.addDetails()

            def deleteDetails():
                """
    Description:
        This function is used for calling delete method of Address book manage class
       
    """
                address.removeDetails()

            def updateDetails():
                """
    Description:
        This function is used for calling update method of Address book manage class
       
    """
                address.updateDetails()

            def displayDetails():
                """
    Description:
        This function is used for calling display method of Address book manage class
       
    """
                address.displayDetails()

            def quit():
                """
    Description:
        This function is used for exiting the program
       
    """
                print('Good bye!!')
                exit()
        
            address.openFile()  # opening the file
            # Asks user for input
            print(' \n 1. Add new contact \n 2. Delete Contacts \n 3. Update AddressBook \n 4. Display AddressBook \n 5. exit')
            menu = {"1":addDetails,"2":deleteDetails ,"3":updateDetails,"4":displayDetails,"5":quit}
            choice = (input("Enter your choice: "))
            toDo = menu.get(choice)
            toDo()
         

    except ValueError:
        logging.error("Enter a valid Input")

    except Exception as e:
        logging.error(e)

