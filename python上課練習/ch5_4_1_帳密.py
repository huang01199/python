while True:
    a=input("請輸入帳號")
    b=input("請輸入密碼")
    if a == "abc":
        if b=="123":
            break
        else:
            print("密碼輸入錯誤，重新輸入")
    else:
        print("帳號輸入錯誤，重新輸入")