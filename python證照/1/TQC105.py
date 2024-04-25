#請撰寫一程式，讓使用者輸入兩個正整數，計算兩個正整數的總和後開根號（四捨五入至小數點後第二位）
a=eval(input())
b=eval(input())
c=(a+b)**0.5
print("result={:.2f}".format(c))
