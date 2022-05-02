import re

wordUnigram = {}

f = open("KCC150_Korean_sentences_UTF8.txt")
lines = f.readlines()
f.close()

for line in lines:
    koreanLineWithSpaceList = re.compile('[ 가-힣]').findall(line)
    koreanLineWithSpace = "".join(koreanLineWithSpaceList)
    koreanLineForWord = " ".join(koreanLineWithSpace.split())
    koreanLineForWord = "_ " + koreanLineForWord + " -"
    koreanWordsList = koreanLineForWord.split(" ")
    for word in koreanWordsList:
        if word in wordUnigram:
            wordUnigram[word] += 1
        else:
            wordUnigram[word] = 1

print("KCC150 끝")

f = open("KCC940_Korean_sentences_UTF8_V2.txt")
lines = f.readlines()
f.close()

for line in lines:
    koreanLineWithSpaceList = re.compile('[ 가-힣]').findall(line)
    koreanLineWithSpace = "".join(koreanLineWithSpaceList)
    koreanLineForWord = " ".join(koreanLineWithSpace.split())
    koreanLineForWord = "_ " + koreanLineForWord + " -"
    koreanWordsList = koreanLineForWord.split(" ")
    for word in koreanWordsList:
        if word in wordUnigram:
            wordUnigram[word] += 1
        else:
            wordUnigram[word] = 1

print("KCC940 끝")

f = open("KCCq28_Korean_sentences_UTF8_v2.txt")
lines = f.readlines()
f.close()

for line in lines:
    koreanLineWithSpaceList = re.compile('[ 가-힣]').findall(line)
    koreanLineWithSpace = "".join(koreanLineWithSpaceList)
    koreanLineForWord = " ".join(koreanLineWithSpace.split())
    koreanLineForWord = "_ " + koreanLineForWord + " -"
    koreanWordsList = koreanLineForWord.split(" ")
    for word in koreanWordsList:
        if word in wordUnigram:
            wordUnigram[word] += 1
        else:
            wordUnigram[word] = 1

wordWriteFile = open("wordUnigramCount.txt", 'w')
for key in wordUnigram.keys():
    wordWriteFile.write(key + " " + str(wordUnigram[key]) + "\n")
wordWriteFile.close()