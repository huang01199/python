def compute(a):
    b=0
    for i in a:
        if i%3==0:
            b=b+1
    return b
a=list(eval(input())for i in range(6))
print(compute(a))