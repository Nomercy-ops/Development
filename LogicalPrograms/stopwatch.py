"""
@Author: Rikesh Chhetri
@Date: 2021-06-29 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-06-29 11:13:30
@Title : Program Aim is to Stimulate a Stopwatch. 
"""

import time

def stopwatch():

  """
    Description:
      This function is used for stimulating stopwatch.
      Time () is used for calculating elapsed time.

  """
  try:
    input("Enter  to Start:")
    startTime = time.time()
    input("Enter  to Stop Time:")
    endTime = time.time()
    timeElapsed = endTime - startTime
    print("Time elapsed from Start to Stop is: ",timeElapsed, " Sec")

  except Exception as e:
    print(e)

stopwatch()



