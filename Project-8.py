def table(number, multiplier):
    for x in range(multiplier):
        if multiplier != x:
            result = (number * x)
            print(number, " x", x, "is equals to", result)
        else:
            break

table(5,3)