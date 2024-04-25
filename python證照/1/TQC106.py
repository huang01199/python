#請撰寫一程式，讓使用者輸入四個整數，依序分別為點及點的座標值，接著計算兩點距離並輸出（四捨五入至小數點後第二位）
x1=eval(input())
y1=eval(input())
x2=eval(input())
y2=eval(input())
a=((x2-x1)**2+(y2-y1)**2)**0.5
print("{:.2f}".format(a))