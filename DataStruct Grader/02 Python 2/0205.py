sss, mode = input("Enter String and Number of Function : ").split(' ')
mode = int(mode)
if mode == 1 :
    print(len(sss))
elif mode == 2 :
    for i in range(len(sss)) :
        asc = ord(sss[i])
        if asc < 91 :
            print(chr(asc+32), end='')
        else :
            print(chr(asc-32), end='')
elif mode == 3 :
    uuu = ""
    #print(len(sss))
    for i in range(len(sss)-1, -1, -1) :
        uuu = uuu + sss[i]
    print(uuu)
elif mode == 4 :
    vvv = ""
    for i in range(len(sss)) :
        if vvv.find(sss[i]) == -1 :
            vvv = vvv + sss[i]
            print(sss[i], end='')
        else :
            continue
        
