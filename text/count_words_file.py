#data = ''
with open('count_words.txt', 'r') as wordFile:
    data = wordFile.read();

print len(data.split())

