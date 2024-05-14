#請撰寫一程式，讓使用者輸入一個1~9位數的數字，輸出每一個數字相乘的算式及結果。
a=input()
b=1
c=""
for i in a:
    b=b*int(i)
    c=c+f"{i}*"
print(f"{c[:-1]}={b}")