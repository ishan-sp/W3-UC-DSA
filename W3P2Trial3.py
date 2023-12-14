total_dist = int(input())
mdt = int(input())
no_stns = int(input())
last_station = 0
stn = list(map(int, input().split()))

#stn = [123, 134, 198, 243, 296, 301, 324, 512, 630, 699, 724, 850, 910]
stn.append(total_dist)
def findmin(dist, stn, mdt):
    found = False
    global last_station
    d = {}
    for j in stn:
        if j <= dist and abs(j - last_station) <= mdt and j > last_station:
            d[dist-j] = j
            found = True
    
    if found:
        min_stn = min(d)
        stn_val = d[min_stn]
        last_station = stn_val
        return stn_val
    else:
        return -1
'''print("T1\n")
print(findmin(200, stn, 200))

print("T2\n")
print(findmin(398, stn, 200))

print("T3\n")
print(findmin(598, stn, 200))

print("T3\n")
print(findmin(798, stn, 200))'''
def notpossible():
    return -1
x = 0
l1 = []
ini = 0
while x != total_dist:
    if -1 in l1:
        print(notpossible())
        break
    if ini == 0:
        x = findmin(mdt, stn, mdt)
        l1.append(x)
        ini += 1
    else:
        x = findmin(last_station+mdt, stn, mdt)
        l1.append(x)
#print(l1)
if -1 not in l1:
    print(len(l1)-1)
#removing the last element from the list l1 as the car need not refuel at the last station as its the end point
#(the program was designed in such a way that comparison was needed from the second last station to the end point so it got included in the final list of sttations for refuelling



    
