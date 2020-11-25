import re
name = input("Enter File :")
if len(name) < 1 : name = "regex_sum_735714.txt"
handle = open(name)
sum = 0
count = 0
for line in handle :
    line = line.rstrip()
    if re.findall('([0-9]+)',line) :
        print(line)
    stuff = re.findall('([0-9]+)',line)
    if len(stuff) < 1 : continue
    #print(stuff)
    for num in stuff :
        sum = sum + int(num)
        count = count + 1
#print(sum)
#print(count)