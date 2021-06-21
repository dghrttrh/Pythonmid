year = int((input("請輸入出生年")))

list1 = ["rat","ox","tiger","rabbit","dragon","snake","horse","sheep","monkey","rooster","dog","pig",]


print(list1[year % 12 - 4])