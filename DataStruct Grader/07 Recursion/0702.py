'''
****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )
เขียน Recursive เพื่อหาว่า String ที่รับเข้ามาเป็น Palindrome หรือไม่
'''
text = input("Enter Input : ")
def isPaliRec(str,i,j) :
    if i == j :
        return True
    if str[i] != str[j] :
        return False
    if i < j+1 :
        return isPaliRec(str,i+1,j-1)
    return True
def isPali(str) :
    n = len(str)
    if n == 0 :
        return True
    return isPaliRec(str,0,n-1)
if isPali(text) :
    print('\'',text,'\''," is palindrome",sep='')
else :
    print('\'',text,'\''," is not palindrome",sep='')
