# 2 is 5 , 5 is 17 , 7 is 25
print("*** Fun with Drawing ***")
n = int(input("Enter input : "))
for i in range(n) :
    for j in range(n - i - 1) :
        print('.', end='')
    print('*', end='')
    for j in range((i * 2) - 1) :
        print('+', end='')
    if i == 0 :
        print('', end='')
    else :
        print('*', end='')
    for j in range((n - 1 - i) * 2 - 1) :
        print('.', end='')

    if i == n - 1 :
        print('', end='')
    else :
        print('*', end='')
    for j in range((i * 2) - 1) :
        print('+', end='')
    if i == 0 :
        print('', end='')
    else :
        print('*', end='')

    for j in range(n - i - 1) :
        print('.', end='')
    print('')
for i in range((n - 1) * 2) :
    for j in range(i + 1) :
        print('.', end='')
    print('*', end='')
    for j in range(-3 + ((n - 1) * 4) - (2 * i)) :
        print('+', end='')
    if i == (((n - 1) * 2) - 1) :
        print('', end='')
    else :
        print('*', end='')
    for j in range(i + 1) :
        print('.', end='')
    print('')