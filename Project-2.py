#There is an array with the name "Names" and it contains the string "Empty".
#Find it and count it how many times it is repeated.

Names = ["Taha", "Ahmed", "Pappu", "Bano", "Banto", "Empty"]

count = 0
for x in range(len(Names)):
    if Names[x] == "Empty" or Names[x]:
        count = count + 1
print("Index number: ", count)