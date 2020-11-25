n = input("Enter String : ")
vvv = ""
lst = []
for i in range(len(n)) :
    if vvv.find(n[i]) == -1 :
        vvv = vvv + n[i]
    else :
        continue
for i in range(len(n)) :
    lst.append(vvv.find(n[i]))
print(lst)