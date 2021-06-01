import random;
number = random.randrange(1,9)
chances = 5

while chances > 0:
    guess = int(input("Guess a number between 1-9. You have 5 chances to guess the number!"))
    
    if guess<number:
        print("You guessed too High!")
        chances = chances -1
        continue
    elif guess>number:
        print("You Guessed too Low!")
        chances = chances -1
        continue
    elif guess==number:
        print("You Guessed Right!!! YOU WON!")
        break
    elif chances == 0:
        print("You ran out of Guesses! The number was" + number)
        break