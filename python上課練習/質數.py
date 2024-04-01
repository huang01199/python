def a(num):
    i=1
    y=0
    while i<=num:
        if(num%i==0):
            y=y+1
        i=i+1    
    if(y==2):
        return True
    else:
        return False    
for b in range(2,101):
    if(a(b)==True):
        print(b,"是質數") 
        