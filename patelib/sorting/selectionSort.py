def selectionSort(data):
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
