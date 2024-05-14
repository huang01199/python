a=eval(input())

for i in range(1,a):
    b=0
    for j in range(1,i+1):
        if i%j==0:
            b=b+1
    if b==2:
        print(f"{i}",end=" ")