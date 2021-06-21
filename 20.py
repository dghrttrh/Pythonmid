list1 = [123, 456, 789, 321, 654]
a = int((input("輸入查詢學號為:")))
b = list1.index(a)
list1[0] = ["Tom", "DTGD"]
list1[1] = ["Cat", "CSIE"]
list1[2] = ["Nana", "ASIE"]
list1[3] = ["Lim", "DBA"]
list1[4] = ["Won", "FDD"]
print("學生資料為:", a, list1[b][0], list1[b][1])