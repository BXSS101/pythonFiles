###################
# Disclaimer part #
###################
'''
HomeWork#3 | Probability Function
Course : Probability & Statistic
Instructor : Asst.prof. Surin Kittitornkun, Ph.D.
Semester / Academic Year : 2 / 2020
Institute : KMITL, Bangkok, Thailand
Developed By :  BXSS101 (Ackrawin B.)
Github URL : https://github.com/BXSS101
'''

################
# Program part #
################
import matplotlib.pyplot as pltA
import csv

#Start Program
print("============================================================")
print("============================================================")
print("    Welcome to thaitourism2.csv data processing program.")
print("============================================================")
#File Selecting
print("    Please Choose a File to Proceed . . . ")
print("        *leave it blank to use default file path")
print("Enter File Path : ", end='')
inPath = input()
#select to display only year or year with months
print("        ↓↓↓ Select display mode to dispaly data ↓↓↓")
print("          \'A\' : Dispaly Month & Year")
print("          \'B\' : Dispaly only Year")
#check if input are in correct format
while True :
    mode = input("          SELECT MODE → ")
    if mode not in ('A', 'a', 'B', 'b', '') :
        print(" !!!!!!!! PLEASE TYPE ONLY A or B !!!!!!!!")
        print(" !!!!!!!!       INPUT AGAIN       !!!!!!!!")
    else :
        break
print("============================================================")
print("============================================================")

#Open File and add Value to List
# 1 # C:/Users/akara/Documents/GitHub/pythonFiles/Prob & Stat/thaitourism2.csv
# 2 # C:/Users/HP/Documents/GitHub/pythonFiles/Prob & Stat/thaitourism2.csv
if inPath == '' :
    path = 'C:/Users/akara/Documents/GitHub/pythonFiles/Prob & Stat/thaitourism2.csv'
else :
    path = inPath
    
#Add open file