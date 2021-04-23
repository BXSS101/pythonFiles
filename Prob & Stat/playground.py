import matplotlib.pyplot as plt4
from statistics import mean
import csv
import time
import math

africa14, africa15, africa16 = [], [], []
path = 'c:/Users/akara/OneDrive - KMITL/Documents/GitHub/pythonFiles/Prob & Stat/thaitourism2.csv'
with open(path, 'r') as file:
    reader = csv.reader(file)
    #process for all year
    for row in reader:
        if row[0] == 'Africa' :
            africa14.append(int(row[2]))
            africa15.append(int(row[3]))
            africa16.append(int(row[4]))

print(africa14)