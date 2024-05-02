#請撰寫一程式，讓使用者輸入兩個正整數a、b，分別輸出a、b的最大公因數和最小公倍數。
def 最大公因數(a,b):
    c=0
    for i in range(1,min(a,b)):
        if a%i==0 and b%i==0:
            c=i
    return c
def 最小公倍數(a,b):
    c=max(a,b)
    while(True):
        if c%a==0 and c%b==0:
            return c
        c=c+1
a=eval(input())
b=eval(input())
print(最大公因數(a,b))
print(最小公倍數(a,b))