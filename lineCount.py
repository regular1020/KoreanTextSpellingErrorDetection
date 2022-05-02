num = 0

f = open("KCC150_Korean_sentences_UTF8.txt")
lines = f.readlines()
f.close()

for line in lines:
    num += 1

f = open("KCC940_Korean_sentences_UTF8_V2.txt")
lines = f.readlines()
f.close()

for line in lines:
    num += 1

f = open("KCCq28_Korean_sentences_UTF8_v2.txt")
lines = f.readlines()
f.close()

for line in lines:
    num += 1

print(num)