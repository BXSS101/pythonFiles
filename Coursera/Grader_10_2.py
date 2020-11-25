name = input("Enter File :")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = dict()
for lines in handle :
    if lines.startswith('From ') :
        lines = lines.split()
        times = lines[5]
        times = times.split(':')
        time = times[0]
        if time not in count :
            count[time] = 1
        else :
            count[time] = count[time] +1
#print(count)
lst = list()
for a,b in count.items() :
    temp = (a, b)
    lst.append(temp)
lst = sorted(lst)
for c, d in lst :
    print(c, d)