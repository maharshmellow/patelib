def binarySearch(data, item):
    found = False
    low = 0
    high = len(data) - 1

    while not found and not(low > high):
        guess = (high-low)//2 + low

        if data[guess] == item:
            found = True
            return(guess)

        elif item < data[guess]:
            high = guess - 1

        elif item > data[guess]:
            low = guess + 1


    return(None)
