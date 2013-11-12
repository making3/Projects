vowels = { 'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0 }
word = raw_input('Enter a word to count vowels for: ')

for c in word.lower():
    if c in vowels:
        vowels[c] += 1

print 'Total vowel counts'
for v in vowels:
    print v + ': ', vowels[v]
