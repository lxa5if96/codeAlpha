import random
animals = ["cat","dog","ant","goat","donkey"]
ranWord = random.choice(animals)
blankSpace = ["_"] * len(ranWord)
wrongGuess = 0
guessLetter = []

while wrongGuess <6 and "_" in blankSpace:
    print(blankSpace)
    print(6 - wrongGuess)
    try:
        letter = input("guess the letter: ").lower()
    except:
        print("Please enter letter only!")
        continue
    
    if len(letter) != 1 or not letter.isalpha():
        print ("Enter One letter (a to z): ")
        continue

    if letter in guessLetter:
        print ("Already Guessed.")
        continue

    guessLetter.append(letter)
    found = False
    for i in range(len(ranWord)):
        if ranWord[i] == letter:
            blankSpace[i] = letter
            found = True
    
    if not found:
        wrongGuess +=1
        print("Wrong Guess.")
    else:
        print("Correct Geuss.")

if "_" not in blankSpace:
    print("you won!")
else:
    print("you lost")
    print("word was:",ranWord)
