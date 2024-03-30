a=int(input("輸入0or1"))
if a == 0:
    for i in range(1,5+1):
        for j in range(1,5+1):
            print(i,"*",j,"=",i*j,"\t",sep="",end="")
        print()
elif a==1:
    for i in range(1,5+1):
        for j in range(1,5+1):
            print(j,"*",i,"=",i*j,"\t",sep="",end="")
        print()
else:
    print("error")