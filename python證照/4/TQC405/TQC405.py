x=list(eval(input())for i in range(3))

with open("read.txt","r") as a:
    c = list(a.readline())
    d = list(a.readline())
    e = list(a.readline())
z=""

for i in range(x[0]):#c 第一行
    c[i]=str(x[0])

for j in range(x[1]):#d 第二行
    d[j]=str(x[1])

for k in range(x[2]):#e 第三行
    e[k]=str(x[2])

z="".join(c)+"".join(d)+"".join(e)
print(z)