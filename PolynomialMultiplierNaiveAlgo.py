import time
'''t1 = eval(input("Enter the first set : "))
t2 = eval(input("Enter the second set : "))'''
t1 = tuple(range(1, 10000))
t2 = tuple(range(1, 10000))
l =[0]*((len(t1)*2)-1)
time1 = time.time()
for j in t1:
    j_ind = t1.index(j)
    for i in t2: 
        i_ind = t2.index(i)
        net_ind = (j_ind + i_ind) 
        l[net_ind] += j*i
time2 = time.time()
#print(tuple(l))
print(time2-time1)

'''(1x + 2x^2.....10000x^10000)
(1x + 2x^2.....10000x^10000)

(1x^1 + 4x^4 + 9x^9 + ....100000000x^100000000)'''
