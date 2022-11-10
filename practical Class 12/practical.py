#Import Section
import pandas as pd
import numpy as np
import time
from matplotlib import pyplot

#Path of CSV
path = "abc.csv"

#Basic SetUp
adaniports_df = pd.read_csv(path)
pd.set_option('display.max_columns', None)

#Various options that are to be displayed on Users Screen
print("-------------------Python and CSV Connectivity-------------------")
print("------------------Currently Available DataFrame------------------")
print("")
print("                Adani Ports Daily Trading Records                ")
print(adaniports_df)
print("")
print("Choose any number to perform a task")
print("Currently available options are:")
print("1.Show DataFrame")
print("2.Find maximum value of any Column")

#Defining Methods

def show_df():
    print(adaniports_df)
    print("Currently Showing DataFrame")

#Running a valid loop
run = True
while run:
    
    #Taking inputs and executing it
    task = int(input("Enter any choice from above: "))

    if task == 1:
        show_df()
    else:
        print("Invalid Choice")

    

