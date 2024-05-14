#請撰寫一程式，讓使用者輸入兩個正整數a、b，請輸出區間［1,a）中，a開根號為正整數且執行下方公式後的所有結果。
a=eval(input())
b=eval(input())
for i in range(1,a):
    if (i**0.5)%1==0:
        print(f"{(i**0.5)**b:.0f}")