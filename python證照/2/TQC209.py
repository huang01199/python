#請撰寫一程式，讓使用者輸入整數0或1，若輸入0則以橫排優先的方式輸出五五乘法表；輸入1則以直排優先的方式輸出五五乘法表；否則輸出「error」。
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
