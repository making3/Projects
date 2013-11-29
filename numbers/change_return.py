import collections
money = float(raw_input('Enter the cost of money to give change for: '))
change = collections.OrderedDict([ 
    ('One-Hundred', 100.00),
    ('Fifty', 50.00),
    ('Twenty', 20.00),
    ('Ten', 10.00),
    ('Five', 5.00),
    ('One', 1.00), 
    ('Quarter', 0.25), 
    ('Dime', 0.10), 
    ('Nickel', 0.05), 
    ('Penny', 0.01) ])

def calcChange(remainder, index = 0):
    coinFactor = change.values()[index]
    coinCount = int(remainder / coinFactor)
    remainder = round(remainder % coinFactor, 2)

    output = {}
    if (index + 1) < len(change):
        output = calcChange(remainder, index + 1)

    output[change.keys()[index]] = coinCount
    return output

def printOutput(outputArray):
    for value in outputArray:
        print value + ': ' + str(outputArray[value])

result = calcChange(money)
printOutput(result)
