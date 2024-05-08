#請撰寫一程式，包含名為compute()的函式，接收主程式傳遞的一個整數n（n ≥ 0），compute()計算n階乘值後回傳至主程式，並輸出n階層結果。
def compute(a):
    b=1
    for i in range(1,a+1):
        b=b*i
    return b
a=eval(input())
print(f"{a}!={compute(a)}")