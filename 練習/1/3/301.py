def compute(a):
    for i in range(a[1]):
        for j in range(a[0]):
            print("*",end="")
        print()
    return a[0]*a[1]
a=list(eval(input())for i in range(2))
print(compute(a))