def 公因數(a,b):
    c=min(a,b)
    d=0
    for i in range(1,c+1):
        if a%i==0 and b%i==0:
            d=i
    return d
def 公倍數(a,b):
    c=max(a,b)
    while(True):
        if c%a==0 and c%b==0:
            return c
        c=c+1
a=eval(input())
b=eval(input())
print(公因數(a,b))
print(公倍數(a,b))
