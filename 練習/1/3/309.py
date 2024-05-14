def compute(a):
    return min(a[0]/a[3],a[1]/a[4],a[2]/a[5])
a=list(eval(input())for i in range(6))
print(f"{compute(a):.3f}")
