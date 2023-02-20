# Make an array with the name "Numbers" and the elements are (10   12   14   76   34   3   2   23)
# find the sum of all the numbers which are greater than 10

Numbers = [10, 12, 14, 76, 34, 3, 2, 23]
Total = 0

for x in range(len(Numbers)):
    if Numbers[x] > 10:
        Total = Total + Numbers

print ("Total of numbers > 10: ", Total)