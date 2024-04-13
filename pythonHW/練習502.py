a = list(input("輸入一個1~9位數的數字: "))
b = [int(i) for i in a]
print(b)
c=1
for i in b:
    c=c*i
print(c)