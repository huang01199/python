#請撰寫一程式，製作簡易計算機，讓使用者依序輸入兩個整數及一個運算符號，輸入「+」代表兩數字相加、「-」代表兩數字相減、「*」代表兩數字相乘，最後將運算結果輸出。
#若輸入「+」、「-」、「*」以外的符號，則輸出「error」。
a=eval(input())
b=eval(input())
c=(input())
if(c=="+"):
    print(a,b,sep="+",end="=")
    print(a+b)
elif(c=="-"):
    print(a,b,sep="-",end="=")
    print(a-b)
elif(c=="*"):
    print(a,b,sep="*",end="=")
    print(a*b)
else:
    print("error")

