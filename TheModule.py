##This is the data module for all things manipulating data
#imports
import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np
#Functions

#Set up
def setup():
    global theconomy
    theconomy = pd.read_csv('TheData.csv')
    theconomy.index.name = "RowNum"
#Viewing full data
def fulldata():
    print(theconomy)
    print("\n \n \n")

#Viewing a visualisation of the data
def visdata():
    print("\nHow would you like your data to be visualised? Press: ")
    time.sleep(1)
    print(" 1. To view the data in a line graph to view a certain value over time\n 2. To view the statistics of a certain year in a bar graph \n 3. To view the data in a scatter plot.\n Or 4. to view the data in a pie chart.")
    time.sleep(1)
    while True:
        try:
            vchoice = int(input("Enter your choice as a number: "))
            break
        except:
            print("ERROR: You entered something other than a number when I asked you to enter a number!") 
        if vchoice == 1:
         print("You have chosen to view a certain value over time in a line graph!")
         while True:
             print("Which variable do you want to measure over time? Enter:")
             time.sleep(1)
             print(" 1. For weekly minimum wage\n 2. For the average weekly grocery price \n 3. For the average weekly rent price\n 4. For the average weekly electricity price\n 5. For the average weekly water bill\n 6. For the total weekly costs\n 7. For the weekly savings\n 8. For minimum wage adjusted for inflation \n 9. For the total weekly costs adjusted for inflation \n Or 10. For the weekly savings adjusted for inflation. ")
             try:
                    vchoice = int(input("Enter your choice as a number here: "))
             except:
                    print("ERROR: You entered something other than a number when I asked you to enter a number!")
             if vchoice == 1:
                  plt.plot(theconomy['year'], theconomy['minin_$'], marker= 'o', linestyle= '-', color= 'red')
                  plt.xlabel("Year") 
                  plt.ylabel("Minimum Wage ($)")
                  plt.yticks(np.arange(0,1100,100))
                  plt.title("Minimum Wage Over The Years")
                  plt.grid()
                  plt.show()
                  break
             elif vchoice == 2:
                   plt.plot(theconomy['year'], theconomy['groceries_$'], marker= 'o', linestyle= '-', color= 'green')
                   plt.xlabel("Year") 
                   plt.ylabel("Average Weekly Grocery Price ($)")
                   plt.yticks(np.arange(0,105,5))
                   plt.title("Average Weekly Grocery Price Over The Years")
                   plt.grid()
                   plt.show()  
                   break             
             elif vchoice == 3:
                  plt.plot(theconomy['year'], theconomy['house_$'], marker= 'o', linestyle= '-', color= 'orange')
                  plt.xlabel("Year") 
                  plt.ylabel("Average Weekly Rent ($)")
                  plt.yticks(np.arange(0,750,50))
                  plt.title("Average Weekly Rent Over The Years")
                  plt.grid()
                  plt.show()    
                  break
             elif vchoice == 4:
                    plt.plot(theconomy['year'], theconomy['electricity_$'], marker= 'o', linestyle= '-', color= 'gold')
                    plt.xlabel("Year") 
                    plt.ylabel("Average Weekly Electricity Bill ($)")
                    plt.yticks(np.arange(0,32,2))
                    plt.title("Average Weekly Electricity Bill Over The Years")
                    plt.grid()
                    plt.show()      
                    break
             elif vchoice == 5:
                 plt.plot(theconomy['year'], theconomy['water_$'], marker= 'o', linestyle= '-', color= 'blue')
                 plt.xlabel("Year") 
                 plt.ylabel("Average Weekly Water Bill ($)")
                 plt.yticks(np.arange(0,5.5,0.5))
                 plt.title("Average Weekly Water Bill Over The Years")
                 plt.grid()
                 plt.show()           
                 break
             elif vchoice == 6:
                    plt.plot(theconomy['year'], theconomy['costtot_$'], marker= 'o', linestyle= '-', color= 'pink')
                    plt.xlabel("Year") 
                    plt.ylabel("Average Necessary Weekly Expenses ($)")
                    plt.yticks(np.arange(0,850,50))
                    plt.title("Average Necessary Weekly Expenses Over The Years")
                    plt.grid()
                    plt.show()       
                    break
             elif vchoice == 7:
                    plt.plot(theconomy['year'], theconomy['savtot_$'], marker= 'o', linestyle= '-', color= 'purple')
                    plt.xlabel("Year") 
                    plt.ylabel("Average Weekly Savings ($)")
                    plt.yticks(np.arange(0,260,10))
                    plt.title("Average Weekly Savings Over The Years")
                    plt.grid()
                    plt.show()       
                    break
             elif vchoice == 8:
                    plt.plot(theconomy['year'], theconomy['todminin_$'], marker= 'o', linestyle= '-', color= 'lime')
                    plt.xlabel("Year") 
                    plt.ylabel("Average Weekly Minimum Wage Adjusted For Inflation ($)")
                    plt.yticks(np.arange(750,960,10))
                    plt.title("Average Weekly Minimum Wage Over The Years (Adjusted for inflation)")
                    plt.grid()
                    plt.show()       
                    break
             elif vchoice == 9:
                    plt.plot(theconomy['year'], theconomy['todcostot_$'], marker= 'o', linestyle= '-', color= 'aqua')
                    plt.xlabel("Year") 
                    plt.ylabel("Average Necessary Weekly Expenses Adjusted For Inflation ($)")
                    plt.yticks(np.arange(500,820,20))
                    plt.title("Average Necessary Weekly Expenses Over The Years (Adjusted for inflation)")
                    plt.grid()
                    plt.show()       
                    break
             elif vchoice == 10:
                    plt.plot(theconomy['year'], theconomy['todsav_$'], marker= 'o', linestyle= '-', color= 'black')
                    plt.xlabel("Year") 
                    plt.ylabel("Average Weekly Savings Adjusted For Inflation ($)")
                    plt.yticks(np.arange(0,320,20))
                    plt.title("Average Weekly Savings Over The Years (Adjusted for inflation)")
                    plt.grid()
                    plt.show()       
                    break
             else:
                    print("ERROR: You entered a number outside of the range of acceptable choices. Please try again.")
                    time.sleep(1)
         break
        if vchoice == 2:
             print("You have chosen to compare the statistics of a certain year in a bar graph! ")
             time.sleep(1)
             while True:
                 pass

     #Dont forget the break that goes here