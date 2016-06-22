class Stack:
    """ADT - First in Last out"""
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if not self.isEmpty():
            return(self.__items.pop())

    def peek(self):
        if not self.isEmpty():
            return(self.__items[len(self.__items)-1])

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
