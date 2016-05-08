def bubbleSort(data):
    """
    Time Complexity
        Best: O(n)
        Average: O(n^2)
        Worst: O(n^2)
    Space Complexity
        Worst: O(1)
    """
    exchange = True
    last = len(data)-1

    while exchange and last >= 0:
        # if no exchanges have been made, the algorithm will stop
        exchange = False
        for current in range(last):
            if (data[current] > data[current+1]):
                # swap the two elements if the left is larger than the right
                temp = data[current]
                data[current] = data[current+1]
                data[current+1] = temp
                # an exchange was made so the sorting will continue
                exchange = True
        # the last section becomes sorted so remove it from the search space
        last -= 1

    return(data)
