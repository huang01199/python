n=int(input("請輸入存的金額"))
x=float(input("請輸入年利率"))
m=int(input("請輸入目標金額"))
i=0
sum=1
while sum>=m:
    b=n*x
    n=n+b
    i=i+1
print(i,"年")
