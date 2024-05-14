a=eval(input())
if a==0:
    for i in range(1,5+1):
        for j in range(1,5+1):
            print(f"{i} x {j} = {i*j}",end="\t")
        print()
elif a==1:
    for i in range(1,5+1):
        for j in range(1,5+1):
            print(f"{j} x {i} = {i*j}",end="\t")
        print()
else:
    print("error")