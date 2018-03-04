def create_tidy_number(number_list, index):
    i = sameNumber[1]
    if sameNumber[0] != 1:
        while i <= index:
            # if number_list[i] == 9:
            #    break
            number_list[i] = number_list[i] - 1
            i = i + 1
    else:
        number_list[sameNumber[1]] = 0
        index = i
    number_list[index + 1:] = [9] * (len(number_list) - index - 1)


fileName = "B-small-practice"
read = open("problems/" + fileName + ".in", "r")
write = open("solutions/" + fileName + ".txt", "w")
size = int(read.readline())
# print(size)

for j in range(size):
    number = read.readline().replace("\n", "")
    numberAsList = [int(x) for x in number]
    sameNumber = [numberAsList[0], 0]
    for i in range(len(numberAsList) - 1):
        if sameNumber[0] != numberAsList[i]:
            sameNumber = [numberAsList[i], i]
        if numberAsList[i] > numberAsList[i+1]:
            create_tidy_number(numberAsList, i)
            break
    # print(numberAsList)
    string = ""
    for x in numberAsList:
        string += str(x)
    result = int(string)
    print(result)
    write.write("Case #" + str(j+1) + ": " + str(result) + "\n")
read.close()
write.close()

