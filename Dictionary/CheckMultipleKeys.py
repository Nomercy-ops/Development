"""
@Author: Rikesh Chhetri
@Date: 2021-07-03 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is to check multiple keys exist or not in dictonary.
"""
from LogHandler import logger

try:
    fruits = {'name': 'apple','price': 'high','size': 'medium'}
    logger.info(fruits.keys() >= {'price', 'name'})
    logger.info(fruits.keys() >= {'name', 'apple'})
    logger.info(fruits.keys() >= {'size', 'name'})

except Exception as e:
    logger.log("Process stopped because %s" % e)
