def compute(a):
    b=0
    for i in range(1,a+1):
        if a%i==0:
            b=b+1
    if b==2:
        return 1
    else:
        return 0
a=eval(input())
if compute(a)==1:
    print(f"{a} is a prime number")
elif compute(a)==0:
    print(f"{a} is not a prime number")