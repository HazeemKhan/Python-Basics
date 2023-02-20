# DECLARE arrayData : Array [ 0 : 9 ]
arrayData = [1, 5, 6, 7, 8, 10, 12, 13, 15, 21]

def BinarySearch(number):
    upperbound = 9  # len (arrayData) - 1
    Lowerbound = 0
    valuefound = False
    notinlist = False

    while valuefound == False and notinlist == False:
        midpoint = int((upperbound + Lowerbound) / 2)

        if arrayData[midpoint] == number:
            valuefound = True
            return True
        elif arrayData[midpoint] < number:
            Lowerbound = midpoint + 1
        else:
            upperbound = midpoint - 1

        if Lowerbound > upperbound:
            notinlist = True
            return False