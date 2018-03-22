fileName = "C-small-practice-1.in"
read = open("problems/" + fileName, "r")
write = open("solutions/" + fileName, "w")
size = int(read.readline())
print(size)

l = read.readline().replace("\n", "").split(" ")
print(l)

read.close()
write.close()
