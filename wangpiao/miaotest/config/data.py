#coding=utf-8

def linxing(i):
    num=(i+1)/2
    for j in range(1,i+1):
        print " "*abs(num-j)+ "*"*(i-(abs(num-j)*2))



i= input("请输入数据的长度")
x=[]

for j in range(1,i):
   str[j]= input("请输入第"+j+"个数组值")

cs=0
js=0
lon=i//2
for a in range(1,i):
    for b in range(a,i):
        if x[a]==x[b]:
            cs=cs+1
    if cs>js:
        js=cs
        y=x[a]

if js>=lon:
    print "出现次数最多的值为"+y+"  共出现了"+js+"次"
else:
    print "没有出现次数超过一半的值"












