#請撰寫一程式，包含名為compute()的函式，接收主程式傳遞的一個陣列，陣列中有三個整數，陣列中索引值1代表運算符號（+或*），若輸入1則索引值前後數值相加；輸入2則相乘，compute()計算運算結果並回傳至主程式輸出。
def compute(a):
    if a[1]==1:
        return a[0]+a[2]
    else:
        return a[0]*a[2]
a=list(eval(input()) for i in range(3))
print(compute(a))
