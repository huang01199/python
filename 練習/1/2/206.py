a=eval(input())
b=eval(input())
c=0
if a%2==0:
    for i in range(a+1,b+1):
        if i%2==1:
            c=c+i
else:
    for i in range(a,b+1):
        if i%2==1:
            c=c+i
print(c)