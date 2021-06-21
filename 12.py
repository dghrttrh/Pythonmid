
b=list(input("輸入一整數列為為:").split())
m=round(len(b)/2)
y=0
x=0
for i in b:
    mon=b.count(i)
    while mon>y:
        y=mon
        x=i
if y>=m:
    print("過半元素為:"+x)

elif y<m:
    print("過半元素為:NO")
