def selectionSort(data):
    """
    Time Complexity
        Best: O(n^2)
        Average: O(n^2)
        Worst: O(n^2)
    Space Complexity
        Worst: O(1)
    """
    for index in range(len(data)):
        smallIndex = index
        # finding smallest
        for i in range(index, len(data)):
            if (data[i] < data[smallIndex]):
                smallIndex = i
        # swapping
        temp = data[index]
        data[index] = data[smallIndex]
        data[smallIndex] = temp

    return(data)
