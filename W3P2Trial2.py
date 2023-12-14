mdt = 200
total_dist = 710
last_station = 0
l2 = [120, 300, 321, 700]
stn = [123, 134, 198, 243, 296, 301, 324, 540, 910]
def findmin(dist, stn, mdt):
    global last_station
    d = {}
    for j in stn:
        if j < dist and j - last_station <= 200:
            d[dist-j] = j
    min_stn = min(d)
    
    print(d)
    stn_val = d[min_stn]
    last_station = stn_val
    return stn_val
print("T1\n")
print(findmin(200, stn, 200))
print("T2\n")
print(findmin(398, stn, 200))
print("T3\n")
print(findmin(598, stn, 200))
