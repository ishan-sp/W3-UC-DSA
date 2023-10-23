#mdt is the maximum distance travelled in one refill of fuel tank
#dist is the distance between the end points
#no_stns is the number of stations present excluding the starting point and including the end point
#stn list is the distances between two consecutive stations
#fstn is the filtered station list excluding the whitespaces generated during input
def findmin(maxd):
    found = False
    for j in stn:
        if maxd-j <= min_dist_left and maxd > j and j - minele < mdt:
            #maxd > j ensures that we dont have negative comparison with least positive distance
            #eg 400-980 = -580 which is lesser than 400-398 = 2. So min element will be set as 980 instead of 398
            #we need it to return 398 instead of 980 which it will return if we dont put maxd > j
            min_dist_left = maxd - j
            minele = j
            found = True

    if found == True:
        return minele
    else:
        return -1

stn= [198, 310, 345, 350, 398, 402, 405, 450, 493, 554, 760]
mdt = int(input("Max dist: "))
total_distance = int(input("Total dist : "))
x = 0
ini = 0
l = []
while total_distance - x >0 :
    if ini == 0 :
        x = findmin(mdt)
        l.append(x)
        ini += 1
    else:
        x = findmin(x + 400)
        l.append(x)
if -1 in l:
    print("Not possible")
else:
    print(l)

