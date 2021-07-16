"""
@Author: Rikesh Chhetri
@Date: 2021-07-03 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is Count of how many dictionaries have success as True.
"""
from LogHandler import logger
try:
  
    sets = [{'id': 1, 'success': True, 'name': 'Lary'}, {
        'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
    count = 0
    # taking from sets as the dictionary does not have multiple values for same keys
    for item in sets:
        if item['success']:
            # the dictionary has the value True at key success in it
            count += 1
    print("The success has the value True ", count, " times")

except Exception as e:
    logger.error(e)
