import re

wordBigram = {}

f = open("KCC150_Korean_sentences_UTF8.txt")

for line in f:
    koreanLineWithSpaceList = re.compile('[ 가-힣]').findall(line)
    koreanLineWithSpace = "".join(koreanLineWithSpaceList)
    koreanLineWithSpace = ' '.join(koreanLineWithSpace.split())
    koreanLineWithSpace = "_ " + koreanLineWithSpace + " -"
    koreanWords = koreanLineWithSpace.split(" ")
    for i in range(len(koreanWords)-1):
        if len(koreanWords[i]) > 3:
            word1 = koreanWords[i][-3:]
        else:
            word1 = koreanWords[i]
        if len(koreanWords[i+1]) > 3:
            word2 = koreanWords[i+1][-3:]
        else:
            word2 = koreanWords[i+1]
        koreanBigram = word1 + " " + word2
        if koreanBigram in wordBigram:
            wordBigram[koreanBigram] += 1
        else:
            wordBigram[koreanBigram] = 1
f.close()
print("KCC150 끝")

f = open("KCC940_Korean_sentences_UTF8_V2.txt")

for line in f:
    koreanLineWithSpaceList = re.compile('[ 가-힣]').findall(line)
    koreanLineWithSpace = "".join(koreanLineWithSpaceList)
    koreanLineWithSpace = ' '.join(koreanLineWithSpace.split())
    koreanLineWithSpace = "_ " + koreanLineWithSpace + " -"
    koreanWords = koreanLineWithSpace.split(" ")
    for i in range(len(koreanWords)-1):
        if len(koreanWords[i]) > 3:
            word1 = koreanWords[i][-3:]
        else:
            word1 = koreanWords[i]
        if len(koreanWords[i+1]) > 3:
            word2 = koreanWords[i+1][-3:]
        else:
            word2 = koreanWords[i+1]
        koreanBigram = word1 + " " + word2
        if koreanBigram in wordBigram:
            wordBigram[koreanBigram] += 1
        else:
            wordBigram[koreanBigram] = 1
f.close()
print("KCC940 끝")

f = open("KCCq28_Korean_sentences_UTF8_v2.txt")

for line in f:
    koreanLineWithSpaceList = re.compile('[ 가-힣]').findall(line)
    koreanLineWithSpace = "".join(koreanLineWithSpaceList)
    koreanLineWithSpace = ' '.join(koreanLineWithSpace.split())
    koreanLineWithSpace = "_ " + koreanLineWithSpace + " -"
    koreanWords = koreanLineWithSpace.split(" ")
    for i in range(len(koreanWords)-1):
        if len(koreanWords[i]) > 3:
            word1 = koreanWords[i][-3:]
        else:
            word1 = koreanWords[i]
        if len(koreanWords[i+1]) > 3:
            word2 = koreanWords[i+1][-3:]
        else:
            word2 = koreanWords[i+1]
        koreanBigram = word1 + " " + word2
        if koreanBigram in wordBigram:
            wordBigram[koreanBigram] += 1
        else:
            wordBigram[koreanBigram] = 1
f.close()
print("KCCq28 끝")


wordBigramFile = open("wordBigramCount.txt", 'w')
for key in wordBigram.keys():
    wordBigramFile.write(key + " " + str(wordBigram[key]) + "\n")
wordBigramFile.close()