n = int(input("整數n:"))
print("數列:%d" %(n),end=" ")
len = 1
while n != 1:
    if n % 2 != 0:
        n = n * 3 + 1
        len += 1
        print(int(n),end=" ")
    else:
        n /= 2
        len += 1
        print(int(n),end=" ")
print("")
print("cycle lengh:",len)