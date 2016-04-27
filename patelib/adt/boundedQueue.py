class BoundedQueue:
    """Queue with a capacity"""
    def __init__(self, capacity):
        self.__items = []
        self.__capacity = capacity
        try:
            if (int(capacity) >= 0):
                pass
            else:
                raise
        except:
            raise

    def enqueue(self, item):
        try:
            if len(self.__items) < self.__capacity:
                self.__items.append(item)
            else:
                raise
        except:
            raise

    def dequeue(self):
        try:
            if len(self.__items) > 0:
                firstElement = self.__items[0]
                self.__items.remove(firstElement)
                return(firstElement)
            else:
                raise
        except:
            raise

    def peek(self):
        try:
            if len(self.__items) > 0:
                firstElement = self.__items[0]
                return(firstElement)
            else:
                raise
        except:
            raise

    def isEmpty(self):
        if len(self.__items) == 0:
            return(True)
        else:
            return(False)

    def isFull(self):
        if len(self.__items) == self.__capacity:
            return(True)
        else:
            return(False)

    def size(self):
        return(len(self.__items))

    def capacity(self):
        return(self.__capacity)

    def clear(self):
        self.__items = []

    def getItems(self):
        # backend way to get the items even though they are meant to be private
        return(self.__items)
        
    def __str__(self):
        return(str(self.__items))
