#請撰寫一程式，讓使用者輸入一個長度不超過50字元的字串，此字串均為小寫字母，輸出該字串出現最多次的英文字母以及出現的次數。
a=input()
b={}
for i in a:
    if i not in b:
        b[i]=1
    else:
        b[i]=b[i]+1

for j,k in b.items():
    if k==max(b.values()):
        print(k)
        print(j)

        

