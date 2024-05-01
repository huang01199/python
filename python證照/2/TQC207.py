#請撰寫一程式，讓使用者輸入大於1的整數，並輸出該數是否為質數。
a=eval(input())
b=0
for i in range(1,a+1):
    if a%i==0:
        b=b+1
if b==2:
    print(f"{a} is a prime number")
else:
    print(f"{a} is not a prime number")