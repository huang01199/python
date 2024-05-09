#請撰寫一程式，包含名為compute()的函式，接收主程式傳遞的一個正整數n（n<10），compute()計算費式數列第n項的值後回傳至主程式，並輸出倒印費氏數列。
def compute(a):
    b=[1,1]
    c=3
    if a==1:
        return [1]
    elif a==2:
        return b
    else:
        for i in range(a-2):
            b.append(b[c-3]+b[c-2])
            c=c+1
        return b

a=eval(input())
for i in range(a,0,-1):
    print(f"fib({i})={compute(a)[i-1]}")
