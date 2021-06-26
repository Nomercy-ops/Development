"""
@Author: Rikesh Chhetri
@Date: 2021-06-26 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-06-26 11:53:30
@Title : Program Aim is to replace string from message with user input string values. 
"""

import re

# storing template in message variables.
message = 'Hello <<username>>, How are you?'


def replace_username(username):
    """replace_username [This function is used for replacing string from a message and used re.sub  to replace oldvalue with newvalue from message]
    Args:
        username ([string]): [This args contains userinput of name and it is used for replacing old value]
    """
    if len(username) >= 3:

        replace = re.sub("<<username>>", username, message)
        print(replace)

    else:
        print("\nstring cannot be replaced..")


# taking user input to replace template string
username = input("\nEnter your First Name : ")
replace_username(username)
