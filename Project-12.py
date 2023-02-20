arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]


def Bubblesort():
    Noswap = False
    Boundary = 9
    while Noswap == False:
        Noswap = True
        for x in range(Boundary):
            if arrayData[x] > arrayData[x + 1]:
                temp = arrayData[x]
                arrayData[x] = arrayData[x + 1]
                arrayData[x + 1] = temp
                Noswap = False
        Boundary = Boundary - 1


Bubblesort()
print(arrayData)
