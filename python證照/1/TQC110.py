#請撰寫一程式，讓使用者輸入三個整數a、b、c，並依序輸出(2)~(4)。
#若a大於等於60且小於100則輸出1，否則輸出0。
#計算b+1再除以10的值，四捨五入至小數點後第二位。
#若a大於等於c，則輸出a，否則輸出c。
a=eval(input())
b=eval(input())
c=eval(input())
if(a>=60 and a<100):
    print("1")
else:
    print("0")
print(f"{(b+1)/10:.2f}")
if(a>=c):
    print(a)
else:
    print(c)