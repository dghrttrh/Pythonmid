a,b = map(int,input("輸入約租費型式及通話時間為:").split())

if a==186:
    if b*0.09//186<=2:
        mon=float(b*0.09*0.9)
    else:
        mon=float(b*0.09*0.8)
if a==386:
    if b*0.08//386<=2:
        mon=float(b*0.08*0.8)
    else:
        mon=float(b*0.08*0.7)       
if a==586:
    if b*0.07//586<=2:
        mon=float(b*0.07*0.7)
    else:
        mon=float(b*0.07*0.6)
if a==986:
    if b*0.06//986<=2:
        mon=float(b*0.06*0.6)
    else:
        mon=float(b*0.06*0.5)

print("通話費為:"+str(round(mon)))