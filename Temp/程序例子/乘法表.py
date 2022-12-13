j = 0
while j < 9:
    j += 1
    i = 1
    while i <= j:
        print(i, "*", j, "=", j * i, end="\t", sep="")
        i += 1
    print("")
