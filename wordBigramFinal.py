bigram1 = {}

f = open("wordBigramCount2.txt")

for line in f:
    key = line.split(" ")[0] + "_" + line.split(" ")[1]
    value = int(line.split(" ")[2])
    bigram1[key] = value

f.close()
print("wordBigram1 finish")

f = open("wordBigramCount.txt")
finalBigramCountText = open("wordBigramCountFinal.txt", "w")

for line in f:
    key = line.split(" ")[0] + "_" + line.split(" ")[1]
    value = int(line.split(" ")[2])
    if key in bigram1:
        value = value + bigram1[key]
        bigram1[key] = 0
    finalBigramCountText.write(key + " " + str(value) + "\n")

f.close()
print("wordBigram2 finish")

for key in bigram1.keys():
    if bigram1[key] > 0:
        finalBigramCountText.write(key + " " + str(bigram1[key]) + "\n")

finalBigramCountText.close()
print("finished")
