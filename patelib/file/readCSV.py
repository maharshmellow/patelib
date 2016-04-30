import csv

def readCSV(fileName, mode):
    """Reads a CSV file and returns a list of the elements"""
    with open(fileName, mode) as f:
        reader = csv.reader(f)
        next(reader)    # skips the column title line
        data = list(reader)
        f.close()
        return(data)
