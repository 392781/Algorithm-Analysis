import random as rand

def select_kth1(list, k):
    list = merge_sort(list)   
    return list[k]

    
    
    
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
    
    
    
    
list = [5,2,3,1,4,5,0]

print(select_kth1(list, 5))