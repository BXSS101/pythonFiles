import math
a = float(input())
ansA = math.pi * math.pow(a, 2)
ansB = a * a * 2
ansA = "{:.6f}".format(ansA)
ansB = "{:.6f}".format(ansB)
print(ansA)
print(ansB)