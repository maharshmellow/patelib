def greatestPrimeFactor(number):
    i = 2
    while number != 1:
        if number % i == 0:
            number = number // i
        else:
            i += 1
    
    return(i)
