class Queue:
    """ADT - First in First Out"""
    def __init__(self):
        self.__items = []

    def queue(self, item):
        self.__items.append(item)

    def dequeue(self):
        if len(self.__items) > 0:
            removedItem = self.__items[0]
            self.__items.remove(removedItem)
            return(removedItem)

    def peek(self):
        if len(self.__items) > 0:
            return(self.__items[0])

    def isEmpty(self):
        return(len(self.__items) == 0)

    def size(self):
        return(len(self.__items))

    def clear(self):
        self.__items = []

    def getItems(self):
        # backend way to get the items even though they are meant to be private
        return(self.__items)

    def __str__(self):
        return(str(self.__items))
