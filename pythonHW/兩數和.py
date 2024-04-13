a=(input("輸入任意長度串列:").split())
num=[int(i) for i in a]
b=int(input("請輸入目標數"))
print("nums =",num,",","target =",b)
x=0
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]+num[j]==b:
            print([i,j])
            x=x+1
if(x==0):
    print("not in list")    