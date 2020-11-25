def eachLines(m ,n) :
    if m == n :
        #print("m =",m,'n =',n)
        print('#',end='')
        eachLines(m,n)
    else :
        #print("m =",m,'n =',n)
        print('_',end='')
        eachLines(m-1,n)

def staircase(i, j) :
    if i == 0 :
        pass
    else :
        staircase(i-1 ,j)
        print("i =",i,'j =',j)
        eachLines(j, i)
    
staircase(3, 3)