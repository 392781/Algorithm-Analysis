import random as rand

def select_kth1(list, k):
    list = merge_sort(list)   
    return list[k]
    
    
    
    
def select_kth2(list, k):
    

  
    
    
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
    
def swap(list, pos1, pos2):
    val = list[pos1]
    list[pos1] = list[pos2]
    list[pos2] = val
    return list
    
    
def partition(list, index):
    val = list[index]
    list = swap(list, index, len(list) - 1)
    
    stored = 0
    for i in range(list):
        if (list[i] < val):
            list = swap(list, stored, i)
            stored += 1
    list = swap(list, len(list) - 1, stored)
    
    return 
    
    
    
    

    
    
    
    
list = [5,2,3,1,4,5,0]

print(select_kth1(list, 5))