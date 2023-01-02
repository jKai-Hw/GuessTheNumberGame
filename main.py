import sys
import random

def startGame():
    while(True):
        minNum = int(input('Type the minimum number: '))
        maxNum = int(input('Type the muximum number: '))
        
        if minNum >= maxNum:
            print('The minimum number entered exceeds the maximum number entered. Please start over from the beginning.The maximum number must exceed the minimum number. Start over from the beginning.')
            continue
        
        ans = {'maxNum':maxNum, 'minNum':minNum}

        return ans

def main():
    numArr = startGame()

    minNum = numArr.get('minNum')
    maxNum = numArr.get('maxNum')
    randomNum = random.randint(minNum, maxNum)

    while(True):
        guessNum = int(input("Let's enter the number you think this is."))

        if guessNum == randomNum:
            print("Per! Congratulations!")
            break
        else:
            print("Shame! Outlier. Let's enter it again.")
            continue

main()