from ValidateInput import ValidateDetails
from LoggerHandler import logger
import json
import numpy as np


class stock():

    # constructor for file handling
    def __init__(self, filename):
        
        try:
            with open(filename) as f:
                self.data = json.load(f) 
        except FileNotFoundError:
            logger.error("file not found")

    # @add stock
    def addStock(self):
        """
    Description:
        This method is used for Adding stocks data into json file.
    
    Parameter:
        It takes self as a parameter 

    Return:
        It return json data and stock dictionary.

    """
        try:  

            stock = ValidateDetails.validateName()
            total_share = int(input("number of share you want to buy : "))
            share_price = np.random.randint(100, 200)

            stockDictionary = {"stock": stock, "total_share": total_share, "share_price": share_price}
            jsonData = self.data
            jsonData.append(stockDictionary)
            return  jsonData,stockDictionary

        except ValueError:  
            logger.info("check the input data")

 
    def showStockReport(self):
        """
    Description:
        This method is used for Displaying all stock details.
    
    Parameter:
        It takes self as a parameter 

    Return:
        It return share_price, total_share, share  of the stock.

    """
      
        share_price = 0
        total_share = 0
        share = 0
        # @for loop is used for traversing the dictonary
        for stocks in range(len(self.data)):
            share += 1
            share_price = share_price + self.data[stocks]["share_price"]
            total_share = total_share + self.data[stocks]["total_share"]

        return share_price, total_share, share


    def deleteStock(self):  # this function is used for deleting the stock
        """
    Description:
        This method is used for Deleting the stock values
    
    Parameter:
        It takes self as a parameter 

    Return:
        It return the value of the index.

    """

        user = input("stock name to delete from the portfolio :")
        stockIndex = -1

        for i in self.data:
            stockIndex += 1

            if i['stock'] == user:
                del self.data[stockIndex]  # data is deleted from the json file
                return stockIndex  # here we have a return value of the index


    def writeData(self):
        """
    Description:
        This method is used for writing stock values into json file.
    
    Parameter:
        It takes self as a parameter 

    """
        with open("stock.json",'w') as f:
            json.dump(self.data,f,indent=2)


    def availableStocks(self): 
        """
    Description:
        This method is used for Displaying remaining or available stocks after deletion.
    
    Parameter:
        It takes self as a parameter 

    Return:
        REmaining stocks values.

    """
        stocks = []
        for i in range(len(self.data)):
            stocks.append(self.data[i]["stock"])

        return stocks  