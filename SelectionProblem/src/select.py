import sys
import time
import random as r

def select_1(arr, left, right, k):
    """ 
    Selection algorithm using mergesort O(n log(n)). Sorts the array
    and returns k-th smallest element.
        
    Parameters:
        arr     (list):         list of integers
        *left   (int):          left index of list
        *right  (int):          right index of list
        k       (int):          k-th smallest element to find
        
        *These arguments aren't needed but are used for the run function
        
    Returns:
        arr[k]  (int):          k-th smallest element of list
    """
    
    arr = merge_sort(arr)
    return arr[k]
     
    
def select_2(arr, left, right, k):
    """ 
    Iterative quickselect algorithm O(n^2).  Uses partition to sort elements
    around a pivot element and look for k-th smallest element.
        
    Parameters:
        arr     (list):         list of integers
        left    (int):          left index of list
        right   (int):          right index of list
        k       (int):          k-th smallest element to find
    
    Returns:
        arr[k]  (int):          k-th smallest element of list
    """
    
    if (left == right):
        return arr[left]
    while(len(arr)):
        pivot = left
        pivot, arr = partition(arr, left, right, pivot)
        
        if (k == pivot):
            return arr[k]
        elif (k < pivot):
            right = pivot - 1
        else:
            left = pivot + 1
    
    
def select_3(arr, left, right, k):
    """ 
    Recursive quickselect algorithm O(n^2).  Uses partition to sort elements
    around a pivot element and look for k-th smallest element.
        
    Parameters:
        arr     (list):         list of integers
        left    (int):          left index of list
        right   (int):          right index of list
        k       (int):          k-th smallest element to find
    
    Returns:
        arr[k]  (int):          k-th smallest element of list
    """
    
    if (left == right):
        return arr[left]
        
    pivot = left
    pivot, arr = partition(arr, left, right, pivot)
    
    if (k == pivot):
        return arr[k]
    elif (k < pivot):
        return select_3(arr, left, pivot - 1, k)
    else:
        return select_3(arr, pivot + 1, right, k)
        
    
def select_4(arr, left, right, k):
    """ 
    Recursive median of medians selection O(n).  Uses the median of medians
    function to select an optimal pivot to then use the quickselect partition 
    function to sort elements around it and look for the k-th smallest element.
        
    Parameters:
        arr     (list):         list of integers
        left    (int):          left index of list
        right   (int):          right index of list
        k       (int):          k-th smallest element to find
    
    Returns:
        arr[k]  (int):          k-th smallest element of list
    """
    
    if (left == right):
        return arr[left]
    
    val = med_of_meds(arr[left:right])
    pivot = arr.index(val)
    pivot, arr = partition(arr, left, right, pivot)
        
    if (k == pivot):
        return arr[k]
    elif (k < pivot):
        return select_4(arr, left, pivot - 1, k)
    else:
        return select_4(arr, pivot + 1, right, k)
    

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''  
    
    
def merge_sort(arr):
    """ 
    Mergesort algorithm used in select_1.  Recursively splits the list
    into sublists that are then merged back together and sorted.
        
    Parameters:
        arr     (list):         list of integers
    
    Returns:
        result  (list):         sorted list
    """
    
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
    """ 
    Part of mergesort.  Merges the split lists back together
        
    Parameters:
        left    (list):          left list
        right   (list):          right list 
    
    Returns:
        result  (list):          merged list
    """
    
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
    """ 
    Part of select_4.  Recursively finds the median of medians of a given list.
        
    Parameters:
        arr     (list):         list of integers
    
    Returns:
        val     (int):          element inside the list to use as a pivot
    """
    
    subarrs = [arr[i : i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(i)[len(i)//2] for i in subarrs]

    if (len(medians) <= 5):
        val = sorted(medians)[(len(medians))//2]
        return val
    else:
        return med_of_meds(medians)
 

def partition(arr, left, right, index):
    """ 
    Part of select_2, 3, and 4.  Partitions a list based on a given index
        
    Parameters:
        arr     (list):         list of integers
        left    (int):          left index of the list
        right   (int):          right index of the list 
        index   (int):          pivot index
    
    Returns:
        store   (int):          the position of the pivot point
        arr     (list):         partitioned list
    """
    
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
    """ 
    Swaps 2 indices of a list.
        
    Parameters:
        arr     (list):         list of integers
        pos1    (int):          index to be swapped
        pos2    (int):          index to be swapped
    
    Returns:
        arr     (list):         list with the elements swapped
    """
    
    val = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = val 
    
    return arr
    
    
def generate(n):
    """ 
    Generates a n-sized list with random, nonrepeating elements
        
    Parameters:
        n       (int):          number of elements to generate
    
    Returns:
        arr     (list):         generated list
    """
    
    arr = []
    
    for i in range(n):
        included = True
        
        while(included):
            val = r.randint(0, n*n)
            if (val not in arr):
                included = False
                
        arr.append(val)
    
    return arr
        
    
def run(method, n):
    """ 
    Runs and times a specified method on a single generated array
        
    Parameters:
        method  (string):       method to run
        n       (int):          number of elements to generate
    
    Returns:
        exe1    (int):          Execution time for k-th position 0
        exe2    (int):          Execution time for k-th position n/4
        exe3    (int):          Execution time for k-th position n/2
        exe4    (int):          Execution time for k-th position 3n/4
        exe5    (int):          Execution time for k-th position n
    """
    
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
    
    
    
''''''''''''''''''''''''''''''# main #''''''''''''''''''''''''''''''



# Begins with array size 10
n = 10

# Generate data files
file1 = open("data-alg-1.txt", "w")
file2 = open("data-alg-2.txt", "w")
file3 = open("data-alg-3.txt", "w")
file4 = open("data-alg-4.txt", "w")

# Begin test 
for i in range(1, 100):
    # Averages for positions 1, n/2, n/4, 3n/4, and n for each algorithm
    avg_k_1 = [0]*5
    avg_k_2 = [0]*5
    avg_k_3 = [0]*5
    avg_k_4 = [0]*5

    sys.stdout.write("n = " + str(n) + "\n")
    sys.stdout.flush()
    
    # 3 passes for each algorithm
    for j in range(1, 4):
        sys.stdout.write("PASS #%d ALG 1-4: \n" % (j))
        sys.stdout.flush()
        exe_time = run(select_1,n)
        for i in range(0,5):
            avg_k_1[i] += exe_time[i]
            
        exe_time = run(select_2,n)
        for i in range(0,5):
            avg_k_2[i] += exe_time[i]
        
        exe_time = run(select_3,n)
        for i in range(0,5):
            avg_k_3[i] += exe_time[i]
        
        exe_time = run(select_4,n)
        for i in range(0,5):
            avg_k_4[i] += exe_time[i]
    
    # Calculate the average of the 3 passes
    avg_k_1 = [x / 3 for x in avg_k_1]
    avg_k_2 = [x / 3 for x in avg_k_2]
    avg_k_3 = [x / 3 for x in avg_k_3]
    avg_k_4 = [x / 3 for x in avg_k_4]
    
    # Write averages to file
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
