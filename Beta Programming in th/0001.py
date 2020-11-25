#Grading from score
a = int(input())
b = int(input())
c = int(input())
sum = a + b + c
if sum > 79 :
    print("A")
elif sum > 74 :
    print("B+")
elif sum > 69 :
    print("B")
elif sum > 64 :
    print("C+")
elif sum > 59 :
    print("C")
elif sum > 54 :
    print("D+")
elif sum > 49 :
    print("D")
elif sum < 50 :
    print("F")