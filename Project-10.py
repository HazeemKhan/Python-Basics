# DECLARE arrayData: Array[0,9]
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

def linearSearch(Number):
    for x in range(9):
        if arrayData[x] == Number:
            print("The position of the number is: ", x + 1)
            return True
    return False

value = int(input("Enter the Number: "))
found = linearSearch(value)

if found == True:
    print("Found")
else:
    print("Not Found")