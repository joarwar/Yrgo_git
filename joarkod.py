#gissa talet 1-100
import random
hemligtnummer = random.randint(1, 101)
numGuesses = 1
guess = int(input("Gissa vad det hemliga numret är mellan 1-100: "))
while (guess != hemligtnummer):
    if guess > hemligtnummer:
        print ("För högt " + str(guess))
    else:
        print ("För lågt " + str(guess))
    numGuesses += 1
    guess = int(input("Gissa en nummer mellan 1-100: "))
print ("Du hade rätt!")
print ("Det tog dig " +str(numGuesses) + " försök.")