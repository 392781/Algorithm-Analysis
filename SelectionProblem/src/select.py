import random as r

def select_1(list, l, r, k):
    list = merge_sort(list)
    return list[k]
     
    
def select_2(list, l, r, k):   
    if (l == r):
        return list[l]
    while(len(list)):
        pivot = l
        pivot, list = partition(list, l, r, pivot)
        
        if (k == pivot):
            return list[k]
        elif (k < pivot):
            r = pivot - 1
        else:
            l = pivot + 1
    
    
def select_3(list, l, r, k):
    if (l == r):
        return list[l]
        
    pivot = l
    pivot, list = partition(list, l, r, pivot)
    
    if (k == pivot):
        return list[k]
    elif (k < pivot):
        return select_3(list, l, pivot - 1, k)
    else:
        return select_3(list, pivot + 1, r, k)
        
    
def select_4(list, l, r, k):
    if (l == r):
        return list[l]
    
    print(list)
    val = med_of_meds(list)
    pivot = list.index(val)
    list = partition(list, l, r, pivot)
        
    if (k == pivot):
        return list[k]
    elif (k < pivot):
        return select_4(list, l, pivot - 1, k)
    else:
        return select_4(list, pivot + 1, r, k)
    
    
    
    
def merge_sort(list):
    result = list[:len(list)]
    
    if (len(list) > 1):
        middle = len(list) // 2
        left = list[:middle]
        right = list[middle:]
        
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
    

    
    
def partition(list, l, r, index):
    pivotval = list[index]
    list = swap(list, index, r)
    store = l
    
    for i in range(l, r):
        if (list[i] < pivotval):
            swap(list, store, i)
            store += 1
            
    list = swap(list, r, store)
    return store, list
  
  
def med_of_meds(list):
    print(list)
    sublists = [list[i : i + 5] for i in range(0, len(list), 5)]
    print(sublists)
    medians = [sorted(i)[len(i)//2] for i in sublists]
    
    if (len(medians) <= 5):
        val = sorted(medians)[len(medians)//2]
        return val
    else:
        return med_of_meds(medians)
        
        
        
    
def swap(list, pos1, pos2):
    val = list[pos1]
    list[pos1] = list[pos2]
    list[pos2] = val 
    return list

def generate(n):
    list = []
    
    for i in range(n):
        list.append(n)
        n -= 1
    
    return list
    
    
    
list = generate(10)
    #sorted[10,20,30,40,50,60,70,80,90,100]
          #  0  1  2  3  4  5  6  7  8  9
for i in range(len(list)):
    print(select_4(list, 0, len(list) - 1, i))