"""
@Author: Rikesh Chhetri
@Date: 2021-06-29 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-06-29 12:03:30
@Title : Program Aim is to simulate gambler bet game and play untill a condition. 
"""

import random

def start_gamble(stake, goal):
    """
    Description:
        This function is used for getting bet result.
        Here a player start with stake and goal and play the game
        untill his pocket is empty or he has achieved his goal.

    Parameter:
        It takes two parameter stake is a starting amount of a player,
        And goal is the winning amount or target amount to win by player.

    """
    try:
    # defining variables here
        win = 0
        loss = 0
        totalGambles = 0

        while not(stake == 0 or stake == goal): # game will go on untill stake is 0 or goal is reached.
            gamble = random.randint(0, 1)
            totalGambles += 1
            if gamble == 0:
                stake += 1
                print(" Yeh you have won!the Bet ")
                win += 1

            else:
                stake -= 1
                print(" Bad luck!You have lost! the Bet ")
                loss += 1

        print(" You won ", win, " times ")
        print(" You Lost ", loss, " times ")
        print(" Your Total Gamble Played ", totalGambles, " times")
        # Getting the Percentage of Winning
        win_percentage = float((win / totalGambles) * 100)
        print(" Win Percent%", win_percentage)
        # Getting the Percentage of Loosing
        loss_percentage = float((loss / totalGambles) * 100)
        print(" Loss Percent%", loss_percentage)

    except Exception as e:
        print(e)

if __name__ == "__main__":

    print("*********************************************")
    print("          Welcome To Betting World     ")
    print("**********************************************")

    try:
        stake = int(input("Enter the starting stake: "))
        while stake < 2:
            stake = int(input("Please start at least with 2$ : "))

        goal = int(input("Enter a winning goal amount: "))
        while goal < stake:
            goal = int(input("Dear enter an amount greater than your stake!: "))

    except ValueError:
        print("Enter a valid integer value")

start_gamble(stake, goal)
