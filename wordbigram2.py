import re

wordBigram2 = {}
f = open("KCCq28_Korean_sentences_UTF8_v2.txt")

for line in f:
    koreanLineWithSpaceList = re.compile('[ 가-힣]').findall(line)
    koreanLineWithSpace = "".join(koreanLineWithSpaceList)
    koreanWords = koreanLineWithSpace.split(" ")
    for i in range(len(koreanWords)-2):
        koreanBigram = koreanWords[i] + " " + koreanWords[i+1]
        if koreanBigram in wordBigram2:
            wordBigram2[koreanBigram] += 1
        else:
            wordBigram2[koreanBigram] = 1
f.close()
print("KCCq28 끝")

wordBigramFile = open("wordBigramCount2.txt", 'w')
for key in wordBigram2.keys():
    wordBigramFile.write(key + " " + str(wordBigram2[key]) + "\n")
wordBigramFile.close()

print("finish")