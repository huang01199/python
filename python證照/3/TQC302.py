#請撰寫一程式，包含名為compute()的函式，接收主程式傳遞的一個期中考分數，compute()判斷分數值，若分數在0~100以外，則回傳「-1」；若分數大於等於60，則加5分；否則一律加10分，回傳至主程式輸出。
def compute(a):
    if 0<a<=100:
        if a>=60:
            return a+5
        else:
            return a+10
    else:
        return -1

a=eval(input())
print(compute(a))