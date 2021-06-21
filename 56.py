meal = input("請選擇主餐及升級的套餐:")
dri = input("是否升級成大杯飲料:")
fre = input("是否換成大薯:")
a = [0,72,62,82,44,60]
sum = a[int(meal[0])]
if meal[1] == 'A':
    sum += 55
else:
    sum += 68
if dri == '是':
    sum += 7
if fre == '是':
    sum += 13
print("總共為%d元" %(sum))