a=(input("輸入羅馬數字:"))
b={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
for key,num in b.items():
    if a == key:
        print("羅馬數字", a, "=",num)
