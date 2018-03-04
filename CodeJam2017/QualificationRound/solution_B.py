fileName = "B-large-practice.in"
read = open("problems/" + fileName, "r")
write = open("solutions/" + fileName, "w")
size = int(read.readline())
# print(size)

for k in range(size):
    number = read.readline().replace("\n", "")
    numberAsList = [int(x) for x in number]

    i = len(numberAsList) - 1
    while i > 0:
        if numberAsList[i] >= numberAsList[i - 1]:
            i = i - 1
            continue
        numberAsList[i - 1] = numberAsList[i - 1] - 1
        j = i
        while j < len(numberAsList):
            numberAsList[j] = 9
            j = j + 1
        i = i - 1
    string = ""
    for x in numberAsList:
        string += str(x)
    result = int(string)
    print(result)
    write.write("Case #" + str(k+1) + ": " + str(result) + "\n")
read.close()
write.close()

