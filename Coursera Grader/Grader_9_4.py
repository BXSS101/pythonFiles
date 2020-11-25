name = input("Enter File :")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = dict()
for lines in handle :
    if lines.startswith('From ') :
        lines = lines.split()
        sender = lines[1]
        if sender not in count :
            count[sender] = 1
        else :
            count[sender] = count[sender] +1
#print(count)
maxKey = None
maxValue = None
for k, v in count.items() :
    if maxValue is None or v > maxValue :
        maxKey = k
        maxValue = v
print(maxKey, maxValue)