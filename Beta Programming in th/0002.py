c = int(input())
min = 2000000000
max = -2000000000
#print(type(min))
i = 0
while i < c :
    n = int(input())
    if n > max :
        max = n
    if n < min :
        min = n
    i = i +1
print(min)
print(max)