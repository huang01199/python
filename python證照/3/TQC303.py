#請撰寫一程式，包含名為compute()的函式，接收主程式傳遞的一個整數n（n>1），compute()判斷是否為質數，若為質數請回傳「1」，否則回傳「0」至主程式，並輸出該數是否為質數。
def compute(a):
    b=0
    for i in range(1,a+1):
        if a%i==0:
            b=b+1
    if b==2:
        return 1
    else:
        return 0
a=eval(input())
if compute(a)==1:
    print(f"{a} is a prime number")
else:
    print(f"{a} is not a prime number")
