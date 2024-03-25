x = int(input("輸入第一個數:"))
y = int(input("輸入第二個數:"))
if x > y :
    c = x
else:
    c = y
for i in range(2, c):
    if x % i == 0 and y % i == 0:
        print(i)    

if x > y :
    c = x
else:
    c = y
for k in range(c, 2, -1):
    if x % k == 0 and y % k == 0:
        print(k)
        break