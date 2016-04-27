def safeOpen(fileName, mode):
    """
    fileName: name of the first to be opened
    mode: w, r, etc.
    """

    try:
        f = open(fileName, mode)
        return(f)
    except:
        print("I/O error: No such file or directory")
        return(None)
    
