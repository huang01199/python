#請撰寫一程式，讓使用者輸入分數，若分數大於60分，則加10分，否則加5分，最後輸出調整後的分數。
#若使用者輸入的分數在0~100以外，則輸出「error」。
a=eval(input())
if(a<0 or a>100):
    print("error")
else:
    if(a>60):
        print(a+10)
    else:
        print(a+5)