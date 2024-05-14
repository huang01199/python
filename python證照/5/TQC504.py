#請撰寫一程式，讓使用者輸入一正整數，判斷是否為迴文數，若是，請輸出「Yes」；若不是，請輸出「No」。
a=eval(input())
b=int(str(a)[::-1])
if a==b:
    print("Yes")
else:
    print("No")