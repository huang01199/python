def compute(a):
    b=1
    for i in range(1,a+1):
        b=b*i
    return b
a=eval(input())
print(f"{a}!={compute(a)}")