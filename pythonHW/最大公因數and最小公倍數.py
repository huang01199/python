def 公因數(a,b):
    c = 1
    for i in range(1, min(a, b)+1):
        if a%i==0 and b%i==0:
            c = i
    return c  
def 公倍數(a,b):
    i=1
    while(True):
        if a*i==b*i:
            return a*i
            
a=int(input("輸入a:"))
b=int(input("輸入b:"))
print("最大公因數:",公因數(a,b),"最小公倍數",公倍數(a,b))




