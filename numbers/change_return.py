import collections
word = float(raw_input('Enter the cost of money to give change for: '))
#word = 5.31
change = collections.OrderedDict([ ('dollar', 1.00), ('quarter', 0.25), ('dime', 0.10), ('nickel', 0.05), ('penny', 0.01) ])
output = {}

def printChange(remainder, changeIndex):
    if changeIndex >= len(change):
        output['remainder'] = int(remainder);
        return remainder
        
    changeInput = change.values()[changeIndex] 
    output[change.keys()[changeIndex]] = int(remainder // changeInput)
    changeIndex += 1
    print 'Remainder: ' + str(remainder)
    print 'Change Input: ' + str(changeInput)
    print str(int(remainder % changeInput))
    return printChange(remainder % changeInput, changeIndex)

def printOutput(outputArray):
    for value in outputArray:
        print value + ': ' + str(outputArray[value])

printChange(word, 0)
printOutput(output)
