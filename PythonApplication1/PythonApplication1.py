

import random

def rotate(arr, a, b):
    if a < 0:
        return 0;
    if b > len(arr):
        return 0;
    return arr[:a] + arr[a:b][::-1] + arr[b:];


# > < ==
def f1(arr):
    ans = []
    for i in range(len(arr)-1):
        ans.append(1 if (arr[i] > arr[i+1]) else 0 if (arr[i] == arr[i+1]) else -1)
    return ans


def f2(arr):
    d1 = []
    d2 = []
    max_start = 0;
    max_end = 1;
    kurr_znak = arr[0];
    for i in range(1, len(arr)):
        if arr[i] == -1*kurr_znak:
            d1.append([max_start, max_end])
            d2.append(max_end - max_start)
            kurr_znak *= -1
            max_start = i
            max_end = i+1;
        elif arr[i] == kurr_znak:
            max_end += 1
    d1.append([max_start, max_end])
    d2.append(max_end - max_start)

    return [d1, d2]

def maxIndex(arr):
    i = 0
    curr_el = arr[i]
    for j in range(len(arr)):
        if arr[j] > curr_el:
            curr_el = arr[j];
            i = j
    return i



size = 8
arr = [i for i in range(1, size+1)]
print(arr)
arr = rotate(arr, 6, size)
print(arr)

for h in range(1):
    print("H", h)
    print(f1(arr))
    arr1 = f1(arr)

    print(f2(arr1))
    d1, d2 = f2(arr1)
    arr2 = f2(arr1)

    
    print(*d1[maxIndex(d2)])

    temp = d1[maxIndex(d2)]
    arr = rotate(arr, max(temp[0]-1, 0), max(temp[1]-1, 0))
    print(arr)



my_list = [i for i in range(1, size + 1)]
random.shuffle(my_list)
print(my_list)
