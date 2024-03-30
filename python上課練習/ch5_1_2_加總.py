a=int(input("請輸入起始值"))
b=int(input("請輸入終止值"))
c=int(input("請輸入遞增值or遞減值"))
sum=0
for i in range(a,b,c):
    sum=sum+i
print(sum)