#請撰寫一程式，包含名為compute()的函式，接收主程式傳遞的一個陣列，陣列中有兩個正整數，陣列索引值0代表一列要輸出的星星數；索引值1代表共輸出幾列，compute()輸出星星印出的結果並計算總共有幾顆星星回傳至主程式輸出。
def compute(a):
    b=a[0]
    c=a[1]
    for i in range(c):
        for j in range(b):
            print("*",end="")
        print()
    return b*c
a=list(eval(input()) for i in range(2)) 
print(compute(a))
