a = input("輸入一個羅馬數字: ")
b = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
c = 0
v = 0
for symbol in reversed(a):
    value = b[symbol]
    if value < v:
        c -= value
    else:
        c += value
    v = value

print("對應的阿拉伯數字為:",c)


