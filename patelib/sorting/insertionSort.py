def insertionSort(data):
    """
    Time Complexity
        Best: O(n)
        Average: O(n^2)
        Worst: O(n^2)
    Space Complexity
        Worst: O(1)
    """
    for index in range(1, len(data)):
        temp = data[index]
        position = index
        while position > 0 and data[position - 1] > temp:  # shifting
            data[position] = data[position - 1]
            position = position - 1

        data[position] = temp                              # inserting

    return(data)
