a1=0
a2=0
a3=0
a4=0
a5=0
a6=0
a7=0
for i in range(10):
    a=eval(input())
    if a==1:
        a1=a1+1
    elif a==2:
        a2=a2+1
    elif a==3:
        a3=a3+1
    elif a==4:
        a4=a4+1
    elif a==5:
        a5=a5+1
    elif a==6:
        a6=a6+1
    else:
        a7=a7+1
print(f"number1:{a1}")
print(f"number2:{a2}")
print(f"number3:{a3}")
print(f"number4:{a4}")
print(f"number5:{a5}")
print(f"number6:{a6}")
print(f"error:{a7}")

