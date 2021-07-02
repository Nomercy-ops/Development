from ValidateInput import ValidateDetails
from LoggerHandler import logger
import json
from CalculateStock import stock

if __name__ == '__main__':

    while True:
        #passing stock.json file to the stock constructor. and creating objectodf stock class.
        myStock = stock("stock.json")
    
        print ("Welcome to stock management")
        try:
            userinput = int(input("\npress 1 Add stock\npress 2 for portfolio report\npress 3 for removing \npress 4  to exit \n "))   
            if userinput == 1:
                num = int(input(" Enter Your Number of stock u want to add value: "))
                for i in range(num):  
                    myStock.addStock()
                    logger.info("stock is added to the portfolio")

            if userinput == 2:  # if input is 1 then over all report will be printed
                print("number of stocks in the portfolio are ", myStock.showStockReport()[2])
                print("total number of share to hold from all the stocks", myStock.showStockReport()[1])
                print("approx amount paid of per stock in your portfolio is ", myStock.showStockReport()[0])

            if userinput == 3:  # if input is 2 then stock will be deleted
                myStock.deleteStock()
                logger.info("stock have been deleted")
                logger.info(myStock.availableStocks())

            if userinput == 4:  # if input is 3 then program will end
                logger.info("thank you for using the service")
                exit()

        except ValueError as err: 
            logger.error("please check the input ",err)
            myStock.writeData("stock.json")
        
        except Exception as e:
            logger.error(e)
   

    

  