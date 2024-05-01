#請撰寫一程式，讓使用者輸入一正整數，輸出小於此整數內的所有質數，質數後方請接一個半形空格。
a=eval(input())

for i in range(1,a,+1):
    b=0
    for j in range(1,i+1):
        if i%j==0:
            b=b+1
    if b==2:
        print(f"{i}",end=" ")
    i=i+1