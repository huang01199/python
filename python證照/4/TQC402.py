#請撰寫一程式，讓使用者輸入兩個相同長度的字串與一個正整數n，字串長度皆不超過128個字元，依ASCII碼表上的順序比對兩字串前n個字元，最後輸出兩字串前n個字元的比較結果。若使用者輸入正整數n超過字串長度，則輸出「error」。
a=input()
b=input()
n=eval(input())
a1=0
b1=0
if n>len(a) or n>len(b):
    print("error")
else:
    for i in range(n):
        a1=a1+ord(a[i])
        b1=b1+ord(b[i])
    if a1==b1:
        print(a,"=",b)
    elif a1>b1:
        print(a,">",b)
    elif a1<b1:
        print(a,"<",b)