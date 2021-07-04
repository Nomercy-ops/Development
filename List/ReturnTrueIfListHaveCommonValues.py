"""
@Author: Rikesh Chhetri
@Date: 2021-07-04 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 9:03:30
@Title : Program Aim is to write a function that takes two lists and returns True if they have at
         least one common member.

"""
from LogHandler import logger


def findCommonMember(list1, list2):
    """
    Description:
        This function is used ofr finding common items between two lists.

    Parameter:
        It Takes a parameter as  list1 and list 2 for finding common items.

    """
    try:

        for string1 in list1:
            for string2 in list2:
                if string1.lower() == string2.lower():
                    return True
        return False

    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    list1 = ['Prakash', 'Deepak', 'Sunil', 'Vijay', 'Suhas', 'Narayan', 'Ajay']
    list2 = ['Rikesh', 'sunil', 'Manoj']
    logger.info(findCommonMember(list1, list2))
    
