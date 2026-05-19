##This is the data module for all things manipulating data
#imports
import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np
#Lists/variables
rowname = ["year","minin_$","groceries_$","house_$","electricity_$","water_$","costtot_$","savtot_$","todminin_$","todcostot_$","todsav_$"]
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
    print(" 1. To view the data in a line graph to view a certain value over time\n Or 2. To view the minimum wage and expenses of each year in a scatter plot.\n")
    time.sleep(1)
    while True:
        try:
               vchoice = int(input("Enter your choice as a number: "))
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
        elif vchoice == 2:
               print("You have chosen to compare the statistics of a certain year in a bar graph! ")
               time.sleep(1)
               while True:
                      try:
                             vchoice = int(input("Would you like to adjust the numbers for inflation? Press 1 if yes, and 0 if no: "))
                      except:
                             print("ERROR: You didn't enter a number")
                      if vchoice == 1:
                             theconomy.plot(
                                    kind='scatter',
                                    x='todminin_$',
                                    y='todcostot_$',
                                    color='green',
                                    alpha=0.3,
                                    title='Correlation of Weekly Expenses and Minimum Wage (But Inflation)'
                                    )
                             plt.show()
                             break
                      elif vchoice == 0:       
                             theconomy.plot(
                                    kind='scatter',
                                    x='minin_$',
                                    y='costtot_$',
                                    color='green',
                                    alpha=0.3,
                                    title='Correlation of Weekly Expenses and Minimum Wage'
                                    )
                             plt.show()
                             break
                      else:
                             print("ERROR: You didn't enter a 1 or 0. Do that next time.")
               break
        else:
               print("ERROR: Please enter either 1 or 2")

#Editing the data
def edata():
       global theconomy
       while True:
              print("How would you like to edit the data? Press: ")
              time.sleep(1)
              print(" 1. To add a new row/year to the file \n 2. To remove a row from the file \n Or 3. To edit a specific cell")    
              try:
                     echoice = int(input("Enter your choice here: "))
              except:
                     print("ERROR: You did not enter a number. ")
              if echoice == 1:
                     while True:
                             print("You have chosen to add a new row! ")
                             time.sleep(1)
                             templist = []                             
                             try:
                                    tempvar = int(input("Enter the year the new row will be for: "))
                                    templist.append(tempvar)
                                    try:
                                           tempvar = float(input("Enter the minimum wage for that year (with a decimal): "))
                                           templist.append(tempvar)
                                           tempvar = float(input("Enter the average weekly groceries shop for that year (with a decimal): "))
                                           templist.append(tempvar)
                                           tempvar = float(input("Enter the average weekly rent for that year (with a decimal): "))
                                           templist.append(tempvar)
                                           tempvar = float(input("Enter the average weekly electricity bill for that year (with a decimal): "))
                                           templist.append(tempvar)
                                           tempvar = float(input("Enter the average weekly water bill for that year (with a decimal): "))
                                           templist.append(tempvar) 
                                           templist.append(templist[2]+templist[3]+templist[4]+templist[5])       
                                           templist.append(templist[1]-templist[6])   
                                           tempvar = float(input(f"Enter the minimum wage of {templist[1]} for that year but accounted for inflation (with a decimal): "))
                                           templist.append(tempvar)
                                           tempvar = float(input(f"Enter the total costs of {templist[6]} for that year but accounted for inflation (with a decimal): "))
                                           templist.append(tempvar)
                                           templist.append(templist[8]-templist[9])
                                           theconomy.loc[len(theconomy)-1] = templist
                                           print("You should probably save your changes!")
                                           break                              
                                    except:
                                           print("ERROR: You didn't enter a number with a decimal place")       
                             except:
                                    print("ERROR: You did not enter a year.")
                             
                             
                     break
              elif echoice == 2:
                     while True:
                            print("You have chosen to remove a row!")
                            print(f"Here are the list of years you can delete: \n{theconomy["year"]}")   
                            time.sleep(3)                         
                            try:
                                   echoice = int(input("Enter which year's row you would like to delete: "))
                                   break
                            except:
                                   print("ERROR: You did not enter a year!")
                                   time.sleep(1)
                            if echoice in theconomy["year"]:
                                    print("ERROR: You didn't enter a year in the acceptable range! ")
                     tempvar = theconomy.index[theconomy["year"] == echoice]
                     theconomy.drop(index=theconomy.index[tempvar], inplace= True)
                     time.sleep(1)
                     print(f"Here is your data after the change: \n {theconomy}")       
                     print("You should probably save your changes! ")
                     break
              elif echoice == 3:
                     while True:
                            print("You have chosen to edit a specific cell! ")
                            try:
                                   echoice = int(input("Enter which years row you would like to edit: "))
                                   break
                            except:
                                   print("ERROR: You didn't enter a number! ")
                     if echoice in theconomy["year"]:
                      print("ERROR: You did not enter a number within the acceptable range!")
                     while True:
                            tempvar = str(input("Enter the column header of the row you would like to edit: ")).lower()
                            if tempvar in rowname:
                                   break
                            else:
                                   print("ERROR: You did not enter a recognised column name! ")
                     while True:
                            try:
                                   ochoice = float(input("Please enter the value you would like to replace that cell with (include a decimal): "))
                                   break
                            except:
                                   print("ERROR: You didn't enter a number with a decimal!")
                     echoice = theconomy.index[theconomy["year"] == echoice]
                     theconomy.loc[echoice, tempvar] = ochoice
                     print(f"Here is the new dataset: \n{theconomy}")
                     break
              else:
                     print("ERROR: You did not enter a valid choice! ")

#Saving the data
def save():
       theconomy.tocsv("TheData.csv")
       print("Changes saved!")

#Filtering the data
def filter():
       while True:
              print("How would you like to get the specifc data? Press: ")
              time.sleep(1)
              print(" 1. To hide data depending on certain characteristics \n 2. To rearrange the data \n Or 3. To group the years by certain traits. ")
              try:
                     fchoice = int(input("Enter your choice as a number here: "))
              except:
                     print("ERROR: You didn't enter a number")
              if fchoice < 1 or fchoice > 3:
                     print("ERROR: You didn't enter a number within the acceptable range! ")
              else:
                     break
       if fchoice == 1:
              print("You have chosen to filter the data!")
              time.sleep(1)
              while True:
                      print("Enter: ")
       elif fchoice == 2:
              print("You have chosen to rearrange the data! ")
              time.sleep(1)
              while True:
                      print("Enter: ")
       elif fchoice == 3:
              print("You have chosen to group the data! ")
              time.sleep(1)
              while True:
                      print("Enter: ")