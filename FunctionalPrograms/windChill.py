"""
@Author: Rikesh Chhetri
@Date: 2021-06-27 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-06-27 12:03:30
@Title : Program Aim is to calculate the effective temperature of wind chill. 
"""

import math

def calculate_wind_chill():
    """
    Description:
        This function is used for calculating wind chill. 
        It takes a user input of temperature and wind speed for calculating wind chill.   
    """

    try:
        temperature = float(input("Enter the Temperature from '0' to '50': "))
        windSpeed = float(input("Enter the Wind Speed between '3' to '120' : "))
        print(temperature)

        if ((temperature) > 50 or windSpeed > 120 or windSpeed < 3):
            print("Please give the Valid input as Shown in the Statement above!!")
            calculate_wind_chill()
        else:
            windChill = 35.74 + 0.62158 * temperature + (0.4275 * temperature - 35.75) * math.pow(windSpeed, 0.16)
            print("The National Weather Service defines the effective temperature (the wind chill) to be: ", windChill)

    except ValueError:
        print("Enter a valid Integer values")
        calculate_wind_chill()


calculate_wind_chill()
