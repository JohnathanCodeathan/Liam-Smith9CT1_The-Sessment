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
       theconomy.tocsv("TheData.csv", index=False)
       print("Changes saved!")

#Filtering the data
def filter():
       global theconomy
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
                      print("Enter: \n 1. To filter rows \n Or 2. To filter by columns.")
                      try:
                             tempvar = int(input("Enter your choice here: "))
                      except: 
                             print("ERROR: You didn't enter a number!")
                      if tempvar < 3 and tempvar > 0:
                             break
                      else: 
                             print("ERROR: You didn't enter a choice within the acceptable range! ")  
              if tempvar == 1:
                     print("You have chosen to filter rows!")
                     time.sleep(1)
                     while True:
                      print("Enter: \n 1. To search for a keyword \n Or 2. To only show the rows of your choice")
                      try:
                             echoice = int(input("Enter your choice here: "))
                      except: 
                             print("ERROR: You didn't enter a number!")
                      if echoice < 3 and echoice > 0:
                             break
                      else: 
                             print("ERROR: You didn't enter a choice within the acceptable range! ")                              
                     if echoice == 1:
                            fchoice = str(input("Enter the word/number you would like to search for: "))       
                            theconomy4 = theconomy[theconomy.astype(str).apply(lambda smolconomy: smolconomy.str.contains(fchoice)).any(axis=1)]
                            if theconomy4.empty:
                                   print("ERROR: Match not found")
                                   time.sleep(2)
                            else:
                             print(theconomy4)
                             time.sleep(2)
                     elif echoice == 2:
                            print("You have chosen to choose which rows to hide!")
                            time.sleep(1)
                            therows = []
                            while True:
                             try:
                                    fchoice = int(input("Enter how many rows you want to see here: "))

                             except: 
                                    print("ERROR: You didn't enter a number!")
                             if fchoice < len(theconomy) and fchoice > 0:
                                    break
                             else: 
                                    print("ERROR: You didn't enter a choice within the acceptable range! ")
                            for i in range (fchoice):
                                   while True:
                                          try:
                                                 echoice = int(input("Enter the year of the row here: "))
                                          except: 
                                                 print("ERROR: You didn't enter a number!")
                                          if echoice in theconomy["year"].values:
                                                 break
                                          else: 
                                                 print("ERROR: You didn't enter a year that is in the dataframe!")
                                   therows.append(theconomy[theconomy["year"] == echoice])
                            theconomy5 = pd.concat(therows).drop_duplicates()
                            print(f"Here is your filtered dataframe: \n\n {theconomy5}")                               
              elif tempvar ==2:
                     print("You have chosen to filter columns!")
                     time.sleep(1)  
                     while True:
                      print("Enter: \n 1. To search for a keyword \n Or 2. To only show the columns of your choice")
                      try:
                             echoice = int(input("Enter your choice here: "))
                      except: 
                             print("ERROR: You didn't enter a number!")
                      if echoice < 3 and echoice > 0:
                             break
                      else: 
                             print("ERROR: You didn't enter a choice within the acceptable range! ")                              
                     if echoice == 1:
                            fchoice = str(input("Enter the word/number you would like to search for: "))       
                            theconomy4 = theconomy.astype(str).apply(lambda smolconomy: smolconomy.str.contains(fchoice, regex= False)).any()
                            if theconomy4.empty:
                                   print("ERROR: Match not found")
                                   time.sleep(2)
                            else:
                             theconomy5 = theconomy.loc[:, theconomy4]
                             print(theconomy5)
                             time.sleep(2)
                     elif echoice == 2:
                            print("You have chosen to choose which columns to hide!")
                            time.sleep(1)
                            thecolumns = []
                            while True:
                             try:
                                    fchoice = int(input("Enter how many columns you want to see here: "))
                                    if fchoice < len(theconomy.columns) and fchoice > 0:
                                           break
                                    else: 
                                           print("ERROR: You didn't enter a choice within the acceptable range! ")                                    
                             except: 
                                    print("ERROR: You didn't enter a number!")
                            for i in range (fchoice):
                                   while True:
                                          echoice = str(input("Enter the name of the column here: ")) 
                                          if echoice in theconomy.columns:
                                                 break
                                          else: 
                                                 print("ERROR: You didn't enter a column name that is in the dataframe!")
                                   thecolumns.append(echoice)
                            theconomy5 = theconomy[thecolumns]
                            print(f"Here is your filtered dataframe: \n\n {theconomy5}")                   
       elif fchoice == 2:
              print("You have chosen to rearrange the data! ")
              time.sleep(1)
              while True:
                      while True:
                             print("Enter: \n 1. To rearrange by row \n Or 2. To sort by collumn")
                             try:
                                    fchoice = int(input("Enter your choice here: "))
                             except: 
                                    print("ERROR: You didn't enter a number!")
                             if fchoice < 3 and fchoice > 0:
                                    break
                             else: 
                                    print("ERROR: You didn't enter a choice within the acceptable range! ")
                      if fchoice == 1:
                             print("You have chosen to sort by row! ")
                             time.sleep(1)
                             while True:
                                    print("Pick a number from 1-11 which will represent which column you will sort the rows by, with 1 being year, and 11 being todsav_$. ")
                                    try:
                                           fchoice = int(input("Enter your choice here: "))
                                    except: 
                                           print("ERROR: You didn't enter a number!")
                                    if fchoice < 12 and fchoice > 0:
                                           break
                                    else: 
                                           print("ERROR: You didn't enter a choice within the acceptable range! ")
                                    fchoice = fchoice -1
                             while True:
                                    print("Enter: \n 1. To arrange your rows by lowest value to highest value \n 2. To arrange your rows by highest value to lowest value \n Or 3. To set them to default")
                                    try:
                                           tempvar = int(input("Enter your choice here: "))
                                    except: 
                                           print("ERROR: You didn't enter a number!")
                                    if tempvar < 4 and tempvar > 0:
                                           break
                                    else: 
                                           print("ERROR: You didn't enter a choice within the acceptable range! ")                                
                             if tempvar == 1:
                                    theconomy.sort_values(by=theconomy.columns[fchoice], inplace=True)
                                    print(f"Here is the sorted dataframe: \n \n{theconomy}")
                             elif tempvar == 2:
                                    theconomy.sort_values(by= theconomy.columns[fchoice], ascending=False, inplace=True)
                                    print(f"Here is the sorted dataframe: \n \n{theconomy}")
                             elif tempvar ==3:
                                    theconomy.sort_values(by=theconomy.columns["year"], inplace=True)
                                    print(f"Here is the sorted dataframe: \n\n {theconomy}")
                      elif fchoice == 2:
                             print("You have chosen to sort by column! ")
                             time.sleep(1)
                             theconomy3 = pd.DataFrame()
                             templist = []
                             for i in range(11):
                                    while True:
                                           print(f"Columns already placed: {templist}")
                                           try:
                                                  tempvar = int(input(f"Pick a number from 1-11 which will represent which column you want at {i+1}th , with 1 being year, and 11 being todsav_$. ")) -1
                                           except:
                                                  print("ERROR: You didn't enter an acceptable number!")
                                           else:
                                                  if theconomy.columns[tempvar] in theconomy3:
                                                         print("That column is already there! ")
                                                  else:
                                                         break
                                    templist.append(tempvar+1)
                                    theconomy3[theconomy.columns[tempvar]] = theconomy.iloc[:,tempvar]
                             theconomy = pd.DataFrame(theconomy3)
                             print(f"Here is the sorted dataframe: \n\n {theconomy}")
                             time.sleep(1)
                             break
       elif fchoice == 3:
        print("You have chosen to group the data! ")
        time.sleep(1)
        while True:
               print("Press: \n 1. To get a frequency distribution table of a certain column \n or 2. Get the average/range/standard deviation of a standard column ")
               try:
                      tempvar = int(input("Enter your choice here: "))
               except:
                      print("ERROR: You didn't enter a number!")
               if tempvar != 1 and tempvar != 2:
                      print("ERROR: You didn't enter a 1 or a 2!")
               else:
                      break
        if tempvar == 1:
               print("You have chosen to see a frequency distribution table of a certain column!")
               time.sleep(1)
               while True:
                      echoice = str(input("Enter the column you want to do a table on: "))
                      if echoice.lower() in theconomy.columns:
                             break
                      else:
                             print("ERROR: You didnt enter a column name that exists!")
               if echoice.lower() == "year":
                      print("You have chosen to do a frequency distribution table on the year!")  
                      time.sleep(1)
                      print(f'Frequency Distribution table of {echoice}')       
                      print(f"2000>: {(theconomy['year']<2000).sum()}") 
                      print(f"2000-2004: {((theconomy['year']>1999) & (theconomy['year']<2005)).sum()}")
                      print(f"2005-2009: {((theconomy['year']>2004) & (theconomy['year']<2010)).sum()}")   
                      print(f"2010-2014: {((theconomy['year']>2009) & (theconomy['year']<2015)).sum()}")
                      print(f"2015-2019: {((theconomy['year']>2014) & (theconomy['year']<2020)).sum()}")
                      print(f"2020-2024: {((theconomy['year']>2019) & (theconomy['year']<2025)).sum()}")
                      print(f"2025+: {(theconomy['year']>2024).sum()}")
               elif echoice.lower() == "minin_$":
                      print("You have chosen to do a frequency distribution table on the minimum wage!")  
                      time.sleep(1)
                      print(f'Frequency Distribution table of {echoice}')       
                      print(f"400>: {(theconomy['minin_$']<400).sum()}") 
                      print(f"400-499: {((theconomy['minin_$']>399) & (theconomy['minin_$']<500)).sum()}")
                      print(f"500-599: {((theconomy['minin_$']>499) & (theconomy['minin_$']<600)).sum()}")   
                      print(f"600-699: {((theconomy['minin_$']>599) & (theconomy['minin_$']<700)).sum()}")
                      print(f"700-799: {((theconomy['minin_$']>699) & (theconomy['minin_$']<800)).sum()}")
                      print(f"800-899: {((theconomy['minin_$']>799) & (theconomy['minin_$']<900)).sum()}")
                      print(f"900+: {(theconomy['minin_$']>899).sum()}")
               elif echoice.lower() == "groceries_$":
                      print("You have chosen to do a frequency distribution table on the weekly grocery price!")  
                      time.sleep(1)
                      print(f'Frequency Distribution table of {echoice}')       
                      print(f"40>: {(theconomy['groceries_$']<40).sum()}") 
                      print(f"40-49: {((theconomy['groceries_$']>39) & (theconomy['groceries_$']<50)).sum()}")
                      print(f"50-59: {((theconomy['groceries_$']>49) & (theconomy['groceries_$']<60)).sum()}")   
                      print(f"60-69: {((theconomy['groceries_$']>59) & (theconomy['groceries_$']<70)).sum()}")
                      print(f"70-79: {((theconomy['groceries_$']>69) & (theconomy['groceries_$']<80)).sum()}")
                      print(f"80-89: {((theconomy['groceries_$']>79) & (theconomy['groceries_$']<90)).sum()}")
                      print(f"90+: {(theconomy['groceries_$']>89).sum()}")
               elif echoice.lower() == "house_$":
                      print("You have chosen to do a frequency distribution table on the weekly rent price!")  
                      time.sleep(1)
                      print(f'Frequency Distribution table of {echoice}')       
                      print(f"200>: {(theconomy['house_$']<200).sum()}") 
                      print(f"200-299: {((theconomy['house_$']>199) & (theconomy['house_$']<300)).sum()}")
                      print(f"300-399: {((theconomy['house_$']>299) & (theconomy['house_$']<400)).sum()}")   
                      print(f"400-499: {((theconomy['house_$']>399) & (theconomy['house_$']<500)).sum()}")
                      print(f"500-599: {((theconomy['house_$']>499) & (theconomy['house_$']<600)).sum()}")
                      print(f"600-699: {((theconomy['house_$']>599) & (theconomy['house_$']<700)).sum()}")
                      print(f"700+: {(theconomy['house_$']>699).sum()}")
               elif echoice.lower() == "electricity_$":
                      print("You have chosen to do a frequency distribution table on the weekly electricity price!")  
                      time.sleep(1)
                      print(f'Frequency Distribution table of {echoice}')       
                      print(f"5>: {(theconomy['electricity_$']<5).sum()}") 
                      print(f"5-9: {((theconomy['electricity_$']>4) & (theconomy['electricity_$']<10)).sum()}")
                      print(f"10-14: {((theconomy['electricity_$']>9) & (theconomy['electricity_$']<15)).sum()}")   
                      print(f"15-19: {((theconomy['electricity_$']>14) & (theconomy['electricity_$']<20)).sum()}")
                      print(f"20+: {(theconomy['electricity_$']>19).sum()}")
               elif echoice.lower() == "water_$":
                      print("You have chosen to do a frequency distribution table on the weekly water price!")  
                      time.sleep(1)
                      print(f'Frequency Distribution table of {echoice}')       
                      print(f"1>: {(theconomy['water_$']<1).sum()}") 
                      print(f"1-1.99: {((theconomy['water_$']>0.99) & (theconomy['water_$']<2)).sum()}")
                      print(f"2-2.99: {((theconomy['water_$']>1.99) & (theconomy['water_$']<3)).sum()}")   
                      print(f"3-3.99: {((theconomy['water_$']>2.99) & (theconomy['water_$']<4)).sum()}")
                      print(f"4-4.99: {((theconomy['water_$']>3.99) & (theconomy['water_$']<5)).sum()}")
                      print(f"5+: {(theconomy['water_$']>4.99).sum()}")  
               elif echoice.lower() == "costtot_$":
                      print("You have chosen to do a frequency distribution table on the total weekly expenses!")  
                      time.sleep(1)
                      print(f'Frequency Distribution table of {echoice}')       
                      print(f"200>: {(theconomy['costtot_$']<200).sum()}") 
                      print(f"200-299: {((theconomy['costtot_$']>199) & (theconomy['costtot_$']<300)).sum()}")
                      print(f"300-399: {((theconomy['costtot_$']>299) & (theconomy['costtot_$']<400)).sum()}")   
                      print(f"400-499: {((theconomy['costtot_$']>399) & (theconomy['costtot_$']<500)).sum()}")
                      print(f"500-599: {((theconomy['costtot_$']>499) & (theconomy['costtot_$']<600)).sum()}")
                      print(f"600-699: {((theconomy['costtot_$']>599) & (theconomy['costtot_$']<700)).sum()}")
                      print(f"700+: {(theconomy['costtot_$']>699).sum()}")    
               elif echoice.lower() == "savtot_$":
                      print("You have chosen to do a frequency distribution table on the total weekly savings!")  
                      time.sleep(1)
                      print(f'Frequency Distribution table of {echoice}')       
                      print(f"100>: {(theconomy['savtot_$']<100).sum()}") 
                      print(f"100-139: {((theconomy['savtot_$']>99) & (theconomy['savtot_$']<140)).sum()}")
                      print(f"140-179: {((theconomy['savtot_$']>139) & (theconomy['savtot_$']<180)).sum()}")   
                      print(f"180-219: {((theconomy['savtot_$']>179) & (theconomy['savtot_$']<220)).sum()}")
                      print(f"220-259: {((theconomy['savtot_$']>219) & (theconomy['savtot_$']<260)).sum()}")
                      print(f"260-299: {((theconomy['savtot_$']>259) & (theconomy['savtot_$']<300)).sum()}")
                      print(f"300+: {(theconomy['savtot_$']>299).sum()}")           
               elif echoice.lower() == "todminin_$":
                      print("You have chosen to do a frequency distribution table on the minimum wage (adjusted for inflation) !")  
                      time.sleep(1)
                      print(f'Frequency Distribution table of {echoice}')       
                      print(f"750>: {(theconomy['todminin_$']<750).sum()}") 
                      print(f"750-799: {((theconomy['todminin_$']>749) & (theconomy['todminin_$']<800)).sum()}")   
                      print(f"800-849: {((theconomy['todminin_$']>799) & (theconomy['todminin_$']<850)).sum()}")
                      print(f"850-899: {((theconomy['todminin_$']>849) & (theconomy['todminin_$']<900)).sum()}")
                      print(f"900-949: {((theconomy['todminin_$']>899) & (theconomy['todminin_$']<950)).sum()}")
                      print(f"950-999: {((theconomy['todminin_$']>949) & (theconomy['todminin_$']<1000)).sum()}")
                      print(f"1000+: {(theconomy['todminin_$']>999).sum()}")     
               elif echoice.lower() == "todcostot_$":
                      print("You have chosen to do a frequency distribution table on the minimum wage (adjusted for inflation) !")  
                      time.sleep(1)
                      print(f'Frequency Distribution table of {echoice}')       
                      print(f"500>: {(theconomy['todcostot_$']<500).sum()}") 
                      print(f"500-549: {((theconomy['todcostot_$']>499) & (theconomy['todcostot_$']<550)).sum()}")   
                      print(f"550-599: {((theconomy['todcostot_$']>549) & (theconomy['todcostot_$']<649)).sum()}")
                      print(f"600-649: {((theconomy['todcostot_$']>599) & (theconomy['todcostot_$']<650)).sum()}")
                      print(f"650-699: {((theconomy['todcostot_$']>649) & (theconomy['todcostot_$']<700)).sum()}")
                      print(f"700-749: {((theconomy['todcostot_$']>699) & (theconomy['todcostot_$']<750)).sum()}")
                      print(f"750-799: {((theconomy['todcostot_$']>749) & (theconomy['todcostot_$']<800)).sum()}")
                      print(f"800+: {(theconomy['todcostot_$']>799).sum()}")     
               elif echoice.lower() == "todsav_$":
                      print("You have chosen to do a frequency distribution table on the minimum wage (adjusted for inflation) !")  
                      time.sleep(1)
                      print(f'Frequency Distribution table of {echoice}')       
                      print(f"100>: {(theconomy['todsav_$']<100).sum()}") 
                      print(f"100-149: {((theconomy['todsav_$']>99) & (theconomy['todsav_$']<150)).sum()}")   
                      print(f"150-199: {((theconomy['todsav_$']>149) & (theconomy['todsav_$']<200)).sum()}")
                      print(f"200-249: {((theconomy['todsav_$']>199) & (theconomy['todsav_$']<250)).sum()}")
                      print(f"250-299: {((theconomy['todsav_$']>249) & (theconomy['todsav_$']<300)).sum()}")
                      print(f"300+: {(theconomy['todsav_$']>299).sum()}")    
        elif tempvar == 2:
               print("You have chosen to see the average, range, and standard deviation of a certain column! ")
               time.sleep(1)
               while True:
                      echoice = str(input("Enter the column you want to do the average/range/standard deviation on: "))
                      if echoice.lower() in theconomy.columns:
                             break
                      else:
                             print("ERROR: You didnt enter a column name that exists!") 
               print(f"You have chosen to see the average/range/standard deviation of {echoice}!")
               print(f"Mean: {(theconomy[echoice].sum())/len(theconomy)}")
               print(f"Median: {theconomy[echoice].median()}") 
               print(f"Mode: {theconomy[echoice].mode()}")   
               print(f"Range: {(theconomy[echoice].max())-(theconomy[echoice].min())}")
               print(f"Standard Deviation: {theconomy[echoice].std()}")                        