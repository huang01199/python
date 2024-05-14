def compute(a):
    return max(a[0],a[1],a[2],a[3],a[4])
a=list(eval(input())for i in range(5))
print(compute(a))