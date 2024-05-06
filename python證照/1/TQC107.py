#請撰寫一程式，讓使用者輸入六個整數，將每三個整數列印在同一列（整數之間間隔一個空白字元）。
#為了輸出美觀，每個整數給予10個欄位寬，並分別輸出靠右與靠左對齊。
a=eval(input())
b=eval(input())
c=eval(input())
d=eval(input())
e=eval(input())
f=eval(input())
print(f"{a:>10} {b:>10} {c:>10}")
print(f"{d:>10} {e:>10} {f:>10}")
print(f"{a:<10} {b:<10} {c:<10}")
print(f"{d:<10} {e:<10} {f:<10}")