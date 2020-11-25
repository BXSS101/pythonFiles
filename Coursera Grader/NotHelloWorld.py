# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
n = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    num = line[20:26]
    n = n + float(num)
    count = count + 1
avg = n / count
print("Average spam confidence:",avg)