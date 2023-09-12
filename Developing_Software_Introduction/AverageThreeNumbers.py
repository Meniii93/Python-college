counter = 0
theAverageOfNumbers = 0
theLowestNumber = 0
theHighestNumber = 0
sumTotalOfAllNumbers = 0
usersEnteredNumber = 0

print('PLease, enter a number followed be -999')

while usersEnteredNumber != -999:
    usersEnteredNumber = int(input(''))
    counter += 1
    if (counter == 1):
        theLowestNumber = usersEnteredNumber
        theHighestNumber = usersEnteredNumber
        if (usersEnteredNumber!= -999):
        sumTotalOfAllNumbers = sumTotalOfAllNumbers + usersEnteredNumber
        if (usersEnteredNumber < theLowestNumber):
        theLowestNumber = usersEnteredNumber
        if (usersEnteredNumber > theHighestNumber):    
        theHighestNumber = usersEnteredNumber  
        
print(f'Your entered {str(counter - 1)} number')
print(f'The total number you entered is {str(sumTotalOfAllNumbers)}')
print('The average of your entered numbers is' (sumTotalOfAllNumbers / (counter - 1)))
print('The highest number is' str' (theHighestNumber))
print('The lowest number is' str' (theLowestNumber))

