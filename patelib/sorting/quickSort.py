def quickSort(data):
    """
    Time Complexities
        Best: O(nlog(n))
        Average: O(nlog(n))
        Worst: O(n^2)
    Space Complexities
        Worst: O(log(n))
    """
    return quickSort_helper(data, 0, len(data)-1)
    
def quickSort_helper(data, first, last):
    if first < last:
        pivot = partition(data, first, last)    # partition around a pivot
        quickSort_helper(data, first, pivot-1)  # sort first half
        quickSort_helper(data, pivot+1, last)   # sort second half
    return data

def partition(data, first, last):
    pivotValue = data[first]                    # choosing the pivot as the first element in the list
    leftMark = first + 1                        # indicates the end of the first partition
    rightMark = last                            # indicates the beginning of the second partition
    done = False

    while not done:
        while leftMark <= rightMark and data[leftMark] <= pivotValue:
            leftMark += 1                       # shifting the pointer to the right
            
        while rightMark >= leftMark and data[rightMark] >= pivotValue:
            rightMark -= 1                      # shifting the pointer to the left

        if rightMark < leftMark:
            done = True                         # the partitioning is done
        else:
            temp=data[leftMark]
            data[leftMark] = data[rightMark]
            data[rightMark] = temp

    temp = data[first]                          # putting pivot in place
    data[first] = data[rightMark]
    data[rightMark] = temp
    
    return rightMark

