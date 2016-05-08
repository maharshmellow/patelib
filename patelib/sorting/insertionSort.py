def insertionSort(data):
    for index in range(1, len(data)):
        temp = data[index]
        position = index
        while position > 0 and data[position - 1] > temp:  # shifting
            data[position] = data[position - 1]
            position = position - 1

        data[position] = temp                              # inserting

    return(data)
