#請撰寫一程式，讓使用者輸入一個1~4之間的整數，若輸入1，則輸出「one」；若輸入2，則輸出「two」；若輸入3，則輸出「three」；若輸入4，則輸出「four」，若輸入1~4以外的數字，則輸出「error」。
a=eval(input())
if(a==1):
    print("one")
elif(a==2):
    print("two")
elif(a==3):
    print("three")
elif(a==4):
    print("four")
else:
    print("error")