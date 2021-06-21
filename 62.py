list1 = ["蘋果", "香蕉", "葡萄", "藍莓", "橘子"]
a = input("請輸入水果:")
b = list1.index(a)
list1[0] = ["紅色"]
list1[1] = ["黃色"]
list1[2] = ["紫色"]
list1[3] = ["藍色"]
list1[4] = ["橘色"]
print(a, "是", list1[b][0])