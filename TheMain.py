#This is for the main code and stuff
#Menu options: view full data, visualisations, search for specific data, edit the data, exit

#Imports
import time
import sys
import subprocess
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from TheModule import setup, fulldata, visdata, edata, save, filter
#Functions
def disclaimer():
    print("Disclaimer: Please read the readme first. It's called a READ ME for a reason, for you to read. \nIf you don't know anything about this program, check there, it'll have some helpful things, like a video game manual!")
    print("Now wait 5 seconds while you let that sink in. ")
    time.sleep(5)
def TheUI():
     print("Welcome to the data set!\n")
     time.sleep(3)
     print("This data set will prove that it is harder to survive on minimum wage compared to the past!")
     time.sleep(1)     
     while True:
         try:
             bigchoice = int(input("What would you like to do with the program? Press: \n 1. To view the data in its full \n 2. To see various charts of the data \n 3. To search for specific data \n 4. To edit, add to, or delete some data \n 5. to save your changes \n Or 6. to exit the program \nEnter a number here: "))
         except:
             print("ERROR: Hey.")
             time.sleep(1)
             print("Buddy. ")
             time.sleep(1)
             print("Pal. ")
             time.sleep(1)
             print("Friend. ")
             time.sleep(1)
             print("You didn't enter a whole number. ")
             time.sleep(1)
             print("Next time, enter a whole number and only a whole number. ")
             time.sleep(2)
             print("Please?")
         if bigchoice == 1:
             print("\n \n You have chosen to view the data in its full!")
             time.sleep(2)
             fulldata()             
             #GO MY PANDAS
         elif bigchoice == 2:
             print("You have chosen to visualise the data in a chart!")
             time.sleep(2)
             visdata()
         elif bigchoice == 3:
             print("You have chosen to search for the data!")
             #GO MY ELABORATE FILTER FUNCTION
             filter()
         elif bigchoice == 4:
             print("You have chosen to edit the data!")
             time.sleep(2)
             edata()
         elif bigchoice == 5:
             print("Saving changes...")
             time.sleep(2)
             #GO MY SINGLE LINE SAVING PROGRAM
             save()
         elif bigchoice == 6:
             theconomy2 = pd.read_csv("TheData.csv")
             if theconomy.reset_index(drop= True).equals(theconomy2):
                 print("You have unsaved changes that you should save!")
                 while True:
                     try:
                         smolchoice = int(input("Would you like to save? Press 1 if yes, press 2 if no. \n Enter your choice: "))
                     except:
                         print("ERROR: You didn't enter a number!")
                     if smolchoice == 2:
                         print("If you insist, it's your loss.")
                         break
                     elif smolchoice == 1:
                         print("Saving Changes...")
                         time.sleep(3)
                         theconomy.tocsv("TheData.csv", index=False)
                         print("Changes saved!")
                         break
                     else:
                         print("ERROR: You didn't enter a 1 or a 2. ")
             print("Exiting program...")
             time.sleep(3)
             break
         else:
             print("ERROR: The number you entered doesn't do anything! ")






#Things that will actually be used
disclaimer()
setup()
from TheModule import theconomy 
TheUI()