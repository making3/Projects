word = raw_input('Enter a word to check if it\'s a palidrome: ')

if word == word[::-1]:
    print 'It is a palidrome.'
else:
    print 'It is not.' 
