#This is for the main code and stuff
#Menu options: view full data, visualisations, search for specific data, edit the data, exit

#Imports
import time
import sys
import subprocess
import os
import pandas as pt
import matplotlib.pyplot as plt
import numpy as np
from TheModule import setup, fulldata, visdata, edata
#Functions
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
         elif bigchoice == 4:
             print("You have chosen to edit the data!")
             time.sleep(2)
             edata()
         elif bigchoice == 5:
             print("Saving changes...")
             time.sleep(3)
             #GO MY SINGLE LINE SAVING PROGRAM
         elif bigchoice == 6:
             print("Exiting program...")
             time.sleep(3)
             break
         else:
             print("ERROR: The number you entered doesn't do anything! ")






#Things that will actually be used
setup()
TheUI()