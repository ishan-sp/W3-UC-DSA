import time
n = int(input("Enter the number of terms : "))
start_time = time.time()
n1 = 0
n2 = 1
init = 0
for j in range(0, n-1):
    tmp = n1+n2
    if init == 0:
        print(n1, n2, tmp, sep = "\n")
        init += 1
    else:
        print("Fibbonacci (",j+2,") : ",tmp)
    n1 = n2
    n2 = tmp
end_time = time.time()
print(end_time-start_time)
