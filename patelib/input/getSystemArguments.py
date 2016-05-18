import sys

def getSystemArguments():
    if len(sys.argv) > 1:
        # there are some arguments - return them all in a list
        return(sys.argv)

    else:
        # no arguments were passed in when running the program from command line
        return(None)
