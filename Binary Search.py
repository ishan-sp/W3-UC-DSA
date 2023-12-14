l = [10, 20, 30, 40, 50 , 60 , 70]
def binarysearch(array, low, top, key):
    if top<low:
        s = "not found"
        return s
    mid = low + (top-low)//2
    if array[mid] == key:
        return mid
    elif array[mid] < key:
        return binarysearch(array, mid+1, top, key)
    else:
        return binarysearch(array, low, mid-1, key)
print(binarysearch(l, 0, len(l)-1, 10))
                            
