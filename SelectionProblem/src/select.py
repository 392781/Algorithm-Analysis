import sys
import time
import random as r

def select_1(arr, l, r, k):
    arr = merge_sort(arr)
    return arr[k]
     
    
def select_2(arr, l, r, k):   
    if (l == r):
        return arr[l]
    while(len(arr)):
        pivot = l
        pivot, arr = partition(arr, l, r, pivot)
        
        if (k == pivot):
            return arr[k]
        elif (k < pivot):
            r = pivot - 1
        else:
            l = pivot + 1
    
    
def select_3(arr, l, r, k):
    if (l == r):
        return arr[l]
        
    pivot = l
    pivot, arr = partition(arr, l, r, pivot)
    
    if (k == pivot):
        return arr[k]
    elif (k < pivot):
        return select_3(arr, l, pivot - 1, k)
    else:
        return select_3(arr, pivot + 1, r, k)
        
    
def select_4(arr, l, r, k):
    if (l == r):
        return arr[l]
    
    val = med_of_meds(arr[l:r])
    pivot = arr.index(val)
    pivot, arr = partition(arr, l, r, pivot)
        
    if (k == pivot):
        return arr[k]
    elif (k < pivot):
        return select_4(arr, l, pivot - 1, k)
    else:
        return select_4(arr, pivot + 1, r, k)
    
  
    
    
def merge_sort(arr):
    result = arr[:len(arr)]
    
    if (len(arr) > 1):
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]
        
        left = merge_sort(left)
        right = merge_sort(right)
        result = merge(left, right)
        
    return result
    
    
    
    
def merge(left, right):
    result = []
    i = 0
    j = 0
    
    while (i < len(left) and j < len(right)):
        if (left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        
    if (i < len(left)):
        result.extend(left[i:])

    if (j < len(right)):
        result.extend(right[j:])
        
    return result
    

    
  
def med_of_meds(arr):
    subarrs = [arr[i : i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(i)[len(i)//2] for i in subarrs]

    if (len(medians) <= 5):
        val = sorted(medians)[(len(medians))//2]
        return val
    else:
        return med_of_meds(medians)
 


 
def partition(arr, left, right, index):


    pivotval = arr[index]
    arr = swap(arr, index, right)
    store = left

    for i in range(left, right):
        if (arr[i] < pivotval):
            swap(arr, store, i)
            store += 1
        
    arr = swap(arr, right, store)

    return store, arr        
 
    
    
    
def swap(arr, pos1, pos2):
    val = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = val 
    
    return arr

    
    
    
def generate(n):
    arr = []
    
    for i in range(n):
        val = r.randint(0,n*n)
        arr.append(val)
    
    return arr
    
    
    
    
def run(method, n):
    arr = generate(n)
        
    start = time.time()
    method(arr, 0, len(arr) - 1, 0)
    end = time.time()
        
    exe1 = end - start
    
    start = time.time()
    method(arr, 0, n - 1, n//4)
    end = time.time()
        
    exe2 = end - start

    start = time.time()
    method(arr, 0, n - 1, n//2)
    end = time.time()
        
    exe3 = end - start
    
    start = time.time()
    method(arr, 0, n - 1, (3*n)//4)
    end = time.time()
        
    exe4 = end - start
    
    start = time.time()
    method(arr, 0, n - 1, n - 1)
    end = time.time()
        
    exe5 = end - start
    
    return [exe1, exe2, exe3, exe4, exe5]
    
    
    
''' main '''

n = 10

file1 = open("data-alg-1.txt", "w")
file2 = open("data-alg-2.txt", "w")
file3 = open("data-alg-3.txt", "w")
file4 = open("data-alg-4.txt", "w")

for i in range(1, 100):
    avg_k_1 = [0]*5
    avg_k_2 = [0]*5
    avg_k_3 = [0]*5
    avg_k_4 = [0]*5

    sys.stdout.write("n = " + str(n) + "\n")
    sys.stdout.flush()
    
    for j in range(1, 4):
        sys.stdout.write("PASS #%d ALG 1-4: \n" % (j))
        sys.stdout.flush()
        exe_time = run(select_1,n)
        for i in range(0,5):
            avg_k_1[i] += exe_time[i]
            
        exe_time = run(select_1,n)
        for i in range(0,5):
            avg_k_2[i] += exe_time[i]
        
        exe_time = run(select_1,n)
        for i in range(0,5):
            avg_k_3[i] += exe_time[i]
        
        exe_time = run(select_1,n)
        for i in range(0,5):
            avg_k_4[i] += exe_time[i]
    
    avg_k_1 = [x / 5 for x in avg_k_1]
    avg_k_2 = [x / 5 for x in avg_k_2]
    avg_k_3 = [x / 5 for x in avg_k_3]
    avg_k_4 = [x / 5 for x in avg_k_4]
    
    for i in range(0,5):
        file1.write(str(avg_k_1[i]) + "\n")
        file2.write(str(avg_k_2[i]) + "\n")
        file3.write(str(avg_k_3[i]) + "\n")
        file4.write(str(avg_k_4[i]) + "\n")

    file1.write("\n")
    file2.write("\n")
    file3.write("\n")
    file4.write("\n")
    
    print("\nTIMES: ")
    
    print(avg_k_1)
    print(avg_k_2)
    print(avg_k_3)
    print(avg_k_4)

    print("---------------------------------------\n")    
    
    n *= 2

file1.close()
file2.close()
file3.close()
file4.close() 
