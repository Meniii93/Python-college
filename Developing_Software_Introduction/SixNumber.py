

total = 0
count = 0
minimum = 0
maximun = 0
userInput = 0

while userInput != -999:
    userInput = int(input('Enter a number: '))
    total = total + (userInput)
    count += 1
    
    if count == 6:
        break
        
print(f'This is the some of all the numbers you have typed:  {total}')
print(f'Thesee are the amount of numbers you have typed:  {count}')