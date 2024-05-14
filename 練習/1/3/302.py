def compute(a):
    if 0<=a<=100:
        if a>=60:
            return a+5
        else:
            return a+10
    else:
        return -1
a=eval(input())
print(compute(a))