a=(input("輸入羅馬數字:"))
b={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
result=0
c=0
for i in range(len(a)-1):
    if b[a[i]]<b[a[i+1]]:
        result=result-b[a[i]]
    else:
        result=result+b[a[i]]
result += b[a[-1]]
print(result)
