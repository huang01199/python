def compute(a):
    if a[1]==1:
        return a[0]+a[2]
    elif a[1]==2:
        return a[0]*a[2]
a=list(eval(input())for i in range(3))
print(compute(a))