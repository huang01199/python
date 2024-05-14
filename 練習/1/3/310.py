def compute(a):
    d=0
    for i in range(1,a):
        c=0
        b=len(str(i))
        for j in str(i):
            c=c+(int(j)**b)
        if c==i:
            print(i)
            d=d+i
    return d
a=eval(input())
print(compute(a))