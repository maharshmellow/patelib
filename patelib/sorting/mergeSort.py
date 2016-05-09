def merge(left, right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
            
        else:
            result.append(right[j])
            j+=1

    # adding the remaining values from either list to the result
    result += left[i:]
    result += right[j:]
    return result

def mergeSort(data):
    """
    Time Complexity
        Best: nlog(n)
        Average: nlog(n)
        Worst: nlog(n)
    Space Complexity
        Worst: O(n)
    """
    if len(data) <= 1:
        return data
    
    middle = len(data)//2

    left = mergeSort(data[:middle])
    right = mergeSort(data[middle:])

    return merge(left, right)
