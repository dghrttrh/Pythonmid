import math

km = float((input("輸入路程公里數(km):")))
mon = 0
if km <= 1.5:
    mon = 75
else:
    mon = 75 + 5 * math.ceil((km - 1.5) / 0.25)

print("所需車資為:", mon, "元")