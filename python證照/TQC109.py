#請撰寫一程式，讓使用者輸入分數，判斷此分數是否及格（及格分數為60分以上），若及格，則輸出「pass」；若不及格，則輸出「fail」，再判斷此分數為奇數或偶數，若為奇數，則輸出「odd」；若為偶數，則輸出「even」，若輸入的分數不在0~100中，則輸出「error」。
a=eval(input())
if(a>100):
    print("error")
else:
    if(a>=60 and a<=100):
        print("pass")
    else:
        print("fail")
    if(a%2==0):
        print("even")
    else:
     print("odd")
