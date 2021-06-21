a=list(input("輸入依字元為:"))
a1=reversed(a)
ch=""
ch1=""
for i in a:
    ch +=i

for j in a1:
    ch1 +=j

if ch1 in ch:
    print("YES")
elif ch1 not in ch:
    print("NO")
    



map(func, iter1)



