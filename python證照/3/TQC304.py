#請撰寫一程式，包含名為compute()的函式，接收主程式傳遞的一個陣列，陣列中有六個整數，compute()判斷陣列中有幾個3的倍數並回傳至主程式輸出。
def compute(a):
    b=0
    for i in range(6):
        if a[i]%3==0:
            b=b+1
    return b
a=list(eval(input())for i in range(6))
print(compute(a))