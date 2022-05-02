import re

syllableUnigram = {}
syllableBigram = {}
syllableTrigram = {}
wordUnigram = {}

f = open("KCC150_Korean_sentences_UTF8.txt")
lines = f.readlines()
f.close()

for line in lines:
    koreanLineWithSpaceList = re.compile('[ 가-힣]').findall(line)
    koreanLineWithSpace = "".join(koreanLineWithSpaceList)
    koreanWordsList = koreanLineWithSpace.split(" ")
    for word in koreanWordsList:
        for i in range(len(word)):
            if word[i] in syllableUnigram:
                syllableUnigram[word[i]] += 1
            else:
                syllableUnigram[word[i]] = 1
        if (len(word)) >= 2:
            for i in range(len(word)-2):
                if word[i:i+2] in syllableBigram:
                    syllableBigram[word[i:i+2]] += 1
                else:
                    syllableBigram[word[i:i+2]] = 1
        if (len(word)) >= 3:
            for i in range(len(word)-3):
                if word[i:i+3] in syllableTrigram:
                    syllableTrigram[word[i:i+3]] += 1
                else:
                    syllableTrigram[word[i:i+3]] = 1
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
    koreanWordsList = koreanLineWithSpace.split(" ")
    for word in koreanWordsList:
        for i in range(len(word)):
            if word[i] in syllableUnigram:
                syllableUnigram[word[i]] += 1
            else:
                syllableUnigram[word[i]] = 1
        if (len(word)) >= 2:
            for i in range(len(word)-2):
                if word[i:i+2] in syllableBigram:
                    syllableBigram[word[i:i+2]] += 1
                else:
                    syllableBigram[word[i:i+2]] = 1
        if (len(word)) >= 3:
            for i in range(len(word)-3):
                if word[i:i+3] in syllableTrigram:
                    syllableTrigram[word[i:i+3]] += 1
                else:
                    syllableTrigram[word[i:i+3]] = 1
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
    koreanWordsList = koreanLineWithSpace.split(" ")
    for word in koreanWordsList:
        for i in range(len(word)):
            if word[i] in syllableUnigram:
                syllableUnigram[word[i]] += 1
            else:
                syllableUnigram[word[i]] = 1
        if (len(word)) >= 2:
            for i in range(len(word)-2):
                if word[i:i+2] in syllableBigram:
                    syllableBigram[word[i:i+2]] += 1
                else:
                    syllableBigram[word[i:i+2]] = 1
        if (len(word)) >= 3:
            for i in range(len(word)-3):
                if word[i:i+3] in syllableTrigram:
                    syllableTrigram[word[i:i+3]] += 1
                else:
                    syllableTrigram[word[i:i+3]] = 1
        if word in wordUnigram:
            wordUnigram[word] += 1
        else:
            wordUnigram[word] = 1

print("KCCq28 끝")

syllableUnigramWriteFile = open("unigramCount.txt", 'w')
for key in syllableUnigram.keys():
    syllableUnigramWriteFile.write(key + " " + str(syllableUnigram[key]) + "\n")
syllableUnigramWriteFile.close()

syllableBigramWriteFile = open("bigramCount.txt", 'w')
for key in syllableBigram.keys():
    syllableBigramWriteFile.write(key + " " + str(syllableBigram[key]) + "\n")
syllableBigramWriteFile.close()

syllableTrigramWriteFile = open("trigramCount.txt", 'w')
for key in syllableTrigram.keys():
    syllableTrigramWriteFile.write(key + " " + str(syllableTrigram[key]) + "\n")
syllableTrigramWriteFile.close()

wordWriteFile = open("wordCount.txt", 'w')
for key in wordUnigram.keys():
    wordWriteFile.write(key + " " + str(wordUnigram[key]) + "\n")
wordWriteFile.close()