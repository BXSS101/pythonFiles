sss = input()
uState = 0
lState = 0
for i in range(len(sss)) :
    if sss[i].isupper() :
        uState += 1
    else :
        lState += 1
if uState > 0 and lState > 0 :
    print("Mix")
elif uState > 0 and lState == 0 :
    print("All Capital Letter")
elif uState == 0 and lState > 0 :
    print("All Small Letter")