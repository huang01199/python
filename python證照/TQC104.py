#請撰寫一程式，讓使用者輸入兩個浮點數，計算兩浮點數之總和（四捨五入至小數點後第二位）。
a=eval(input())
b=eval(input())
c=a+b
print("total={:.2f}".format(c))