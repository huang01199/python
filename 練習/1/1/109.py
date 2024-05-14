a=eval(input())
if 0<=a<=100:
    if 60<=a:
        print("pass")
    else:
        print("fail")
    if a%2==0:
        print("even")
    else:
        print("odd")
else:
    print("error")