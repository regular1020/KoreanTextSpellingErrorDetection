import csv
import re
from jamo import j2h

wordUnigram = {}
wordBigram = {}

f = open("wordUnigramCount.txt")

for line in f:
    key = line.split(" ")[0]
    value = int(line.split(" ")[1])
    wordUnigram[key] = value
f.close()

f = open("wordBigramCount.txt")

for line in f:
    key = line.split(" ")[0] + "_" + line.split(" ")[1]
    value = int(line.split(" ")[2])
    wordBigram[key] = value
f.close()

chosung_list = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
jungsung_list = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
jongsung_list = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']


def bigramProb(word, beforeWordAll, afterWordAll, beforeWord, afterWord, prob1, prob2):
    answerWord = word
    answerProb1 = prob1
    answerProb2 = prob2
    for i in range(len(word)):
        char = word[i]
        chosung_index = int((ord(char) - 44032) / (21 * 28))
        jungsung_index = int((ord(char) - 44032 - (chosung_index * 21 * 28)) / 28)
        jongsung_index = int(ord(char) - 44032 - (chosung_index * 21 * 28) - (jungsung_index * 28))
        for x in chosung_list:
            if jongsung_index == 0:
                newWord = word[:i] + j2h(x, jungsung_list[jungsung_index]) + word[i+1:]
            else:
                newWord = word[:i] + j2h(x, jungsung_list[jungsung_index], jongsung_list[jongsung_index]) + word[i+1:]
            if len(newWord) > 3:
                newBigram1 = beforeWord + "_" + newWord[-3:]
                newBigram2 = newWord[-3:] + "_" + afterWord
            else:
                newBigram1 = beforeWord + "_" + newWord
                newBigram2 = newWord + "_" + afterWord
            if newBigram1 in wordBigram:
                newProb1 = wordBigram[newBigram1]/wordUnigram[beforeWordAll]
            else:
                newProb1 = 0
            if newBigram2 in wordBigram:
                newProb2 = wordBigram[newBigram2]/wordUnigram[afterWordAll]
            else:
                newProb2 = 0

            if newProb1 > answerProb1 and newProb2 > answerProb2:
                answerWord = newWord
                answerProb1 = newProb1
                answerProb2 = newProb2
    return answerWord, answerProb1

f = open('probabilityErrorDetect2.csv', 'w')
wr = csv.writer(f)

kcc150 = open("KCC150_Korean_sentences_UTF8.txt")

for line in kcc150:
    koreanLineWithSpaceList = re.compile('[ 가-힣]').findall(line)
    koreanLineWithSpace = "".join(koreanLineWithSpaceList)
    koreanLineWithSpace = ' '.join(koreanLineWithSpace.split())
    koreanLineWithSpace = "_ " + koreanLineWithSpace + " -"
    koreanWords = koreanLineWithSpace.split(" ")
    for i in range(1, len(koreanWords)-1):
        tmpList = []
        word = koreanWords[i]
        tmpWord1 = koreanWords[i-1]
        tmpWord2 = koreanWords[i]
        if len(tmpWord1) > 3:
            tmpWord1 = tmpWord1[-3:]
        if len(tmpWord2) > 3:
            tmpWord2 = tmpWord2[-3:]
        bigram1 = tmpWord1 + "_" + tmpWord2
        bigramProb1 = wordBigram[bigram1]/wordUnigram[koreanWords[i-1]]
        tmpWord3 = tmpWord2
        tmpWord4 = koreanWords[i+1]
        if len(tmpWord4) > 3:
            tmpWord4 = tmpWord4[-3:]
        bigram2 = tmpWord3 + "_" + tmpWord4
        bigramProb2 = wordBigram[bigram2]/wordUnigram[koreanWords[i+1]]
        if bigramProb1 < 0.000005 and bigramProb2 < 0.000005:
            newWord, newProb = bigramProb(word, koreanWords[i-1], koreanWords[i+1], tmpWord1, tmpWord4, bigramProb1, bigramProb2)
            if newWord != word:
                tmpList.append(word)
                tmpList.append(newWord)
                tmpList.append(line)
                tmpList.append("n")
                tmpList.append(str(bigramProb1))
                tmpList.append(str(newProb))
                wr.writerow(tmpList)
                break

kcc150.close()

kcc940 = open("KCC940_Korean_sentences_UTF8_V2.txt")

for line in kcc940:
    koreanLineWithSpaceList = re.compile('[ 가-힣]').findall(line)
    koreanLineWithSpace = "".join(koreanLineWithSpaceList)
    koreanLineWithSpace = ' '.join(koreanLineWithSpace.split())
    koreanLineWithSpace = "_ " + koreanLineWithSpace + " -"
    koreanWords = koreanLineWithSpace.split(" ")
    for i in range(1, len(koreanWords) - 1):
        tmpList = []
        word = koreanWords[i]
        tmpWord1 = koreanWords[i - 1]
        tmpWord2 = koreanWords[i]
        if len(tmpWord1) > 3:
            tmpWord1 = tmpWord1[-3:]
        if len(tmpWord2) > 3:
            tmpWord2 = tmpWord2[-3:]
        bigram1 = tmpWord1 + "_" + tmpWord2
        bigramProb1 = wordBigram[bigram1] / wordUnigram[koreanWords[i - 1]]
        tmpWord3 = tmpWord2
        tmpWord4 = koreanWords[i + 1]
        if len(tmpWord4) > 3:
            tmpWord4 = tmpWord4[-3:]
        bigram2 = tmpWord3 + "_" + tmpWord4
        bigramProb2 = wordBigram[bigram2] / wordUnigram[koreanWords[i + 1]]
        if bigramProb1 < 0.000005 and bigramProb2 < 0.000005:
            newWord, newProb = bigramProb(word, koreanWords[i - 1], koreanWords[i + 1], tmpWord1, tmpWord4, bigramProb1,
                                          bigramProb2)
            if newWord != word:
                tmpList.append(word)
                tmpList.append(newWord)
                tmpList.append(line)
                tmpList.append("n")
                tmpList.append(str(bigramProb1))
                tmpList.append(str(newProb))
                wr.writerow(tmpList)
                break

kcc940.close()

kccq28 = open("KCCq28_Korean_sentences_UTF8_v2.txt")

for line in kccq28:
    koreanLineWithSpaceList = re.compile('[ 가-힣]').findall(line)
    koreanLineWithSpace = "".join(koreanLineWithSpaceList)
    koreanLineWithSpace = ' '.join(koreanLineWithSpace.split())
    koreanLineWithSpace = "_ " + koreanLineWithSpace + " -"
    koreanWords = koreanLineWithSpace.split(" ")
    for i in range(1, len(koreanWords) - 1):
        tmpList = []
        word = koreanWords[i]
        tmpWord1 = koreanWords[i - 1]
        tmpWord2 = koreanWords[i]
        if len(tmpWord1) > 3:
            tmpWord1 = tmpWord1[-3:]
        if len(tmpWord2) > 3:
            tmpWord2 = tmpWord2[-3:]
        bigram1 = tmpWord1 + "_" + tmpWord2
        bigramProb1 = wordBigram[bigram1] / wordUnigram[koreanWords[i - 1]]
        tmpWord3 = tmpWord2
        tmpWord4 = koreanWords[i + 1]
        if len(tmpWord4) > 3:
            tmpWord4 = tmpWord4[-3:]
        bigram2 = tmpWord3 + "_" + tmpWord4
        bigramProb2 = wordBigram[bigram2] / wordUnigram[koreanWords[i + 1]]
        if bigramProb1 < 0.000005 and bigramProb2 < 0.000005:
            newWord, newProb = bigramProb(word, koreanWords[i - 1], koreanWords[i + 1], tmpWord1, tmpWord4, bigramProb1,
                                          bigramProb2)
            if newWord != word:
                tmpList.append(word)
                tmpList.append(newWord)
                tmpList.append(line)
                tmpList.append("n")
                tmpList.append(str(bigramProb1))
                tmpList.append(str(newProb))
                wr.writerow(tmpList)
                break

kccq28.close()

f.close()