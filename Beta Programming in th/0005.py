import math
a, b = map(float, input().split(' '))
ans = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
formatted_float = "{:.6f}".format(ans)
print(formatted_float)