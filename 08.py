a=(input("輸入第一行正整數為:"))
b=list(input("第二行中的數字為:").split())
y=0
x=0
for i in b:
    mon=b.count(i)
    while mon>y:
        y=mon
        x=i

if y==1:
    print("每個數字剛好只出現1次")

else:
    print("最大出現數字為:"+x)
    print("出現次數為:"+str(y))
