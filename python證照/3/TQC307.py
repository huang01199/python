#請撰寫一程式，包含名為compute()的函式，接收主程式傳遞的一個陣列，陣列中包含五個整數，compute()判斷陣列的最大值回傳至主程式輸出。
def compute(a):
    return max(a[0],a[1],a[2],a[3],a[4])
a=list(eval(input()) for i in range(5))
print(compute(a))