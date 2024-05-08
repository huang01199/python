#請撰寫一程式，包含名為compute()的函式，接收主程式傳遞的一個整數n（0 < n < 1000），compute()輸出所有小於n的阿姆斯壯數並回傳總和至主程式輸出。
def compute(a):
    e=0
    for i in range(1,a):
        b=str(i)
        c=len(b)
        d=0
        
        for j in b:
            d=d+(int(j)**c)
        if d==i:
            print(i)
            e=e+i
    return e
a=eval(input())
print(compute(a))

