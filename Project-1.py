# Input a name from the user if that name is in the array then print "it is already in there" 
# If it is not then add it into the array

Names = ["Taha", "Ahmed", "Pappu", "Bano", "Banto", "Pappan" ]

name_Inp = input("Enter name to search the list: ")

for x in range (len(Names)) :
    if Names[x] == name_Inp:
        print("Already present on index number: ", x)
        break

else:
    U_Input = input("Name not found, Would you like to add it?. \n [Y]es or [N]o\n")

    if U_Input == "Y" or U_Input == "y":
        Names.append(name_Inp)
        print(Names)
    elif U_Input == "N" or U_Input == "n":
        print("Bye")
    else:
        print("Invalid input")