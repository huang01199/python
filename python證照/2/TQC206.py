#請撰寫一程式，讓使用者輸入兩個整數，其中第一個整數小於或等於第二個整數，計算兩個整數間（包含輸入值）的奇數和。
a=eval(input())
b=eval(input())
c=0
if a%2==0:
    for i in range(a+1,b+1,+2):
        c=c+i
else:
    for i in range(a,b+1,+2):
        c=c+i
print(c)