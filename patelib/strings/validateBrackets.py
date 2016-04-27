from patelib.adt.stack import *

def validateBrackets(string, openers="([{", closers = ")]}"):
    string = string.strip()

    unmatched = [False, False, False]   # True = There is an unmatched pair

    s = Stack()
    for item in string:
        if item in openers:
            # Add to the stack - look for possible matches in the future
            s.push(item)
        elif item in closers:
            # Check if a pair has been made
            if s.size() > 0:
                # Only look at the last element if there is an element in the list
                top = s.peek()
                if openers.index(top) == closers.index(item):
                    # Match found - remove the instance in the stack
                    s.pop()
                else:
                    unmatched[closers.index(item)] = True
            else:
                unmatched[closers.index(item)] = True

    # remove all elements from the stack if there are any remaining
    while s.size() != 0:
        top = s.pop()
        if top in openers:
            unmatched[openers.index(top)] = True
        elif top in closers:
            unmatched[closers.index(top)] = True

    return(not(unmatched[0] or unmatched[1] or unmatched[2]))      # return true if all are false
