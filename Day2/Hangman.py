import random

listed=["apple", "banana","lemon","potato","tomato"]
choosen_word=random.choice(listed)

print(choosen_word)

length=len(choosen_word)
print(length)

placeholder="_"*length

print(placeholder)


correctguess=[]
gameover=False
lives=6


while not gameover:

    guess=str(input("Enter the alphabet: ")).lower()
    display=""

    for letter in choosen_word:
        if letter== guess:
            display+=letter
            correctguess.append(guess)
        elif letter in correctguess:
            display+=letter
            
        else:
            display+="_"
            
            

    print(display)

    if guess not in choosen_word:
        lives-=1
        print(f"Wrong guess! You have {lives} lives left.")
        if lives==0:
            gameover=True
            print("Game Over! You lost.")
            break

    if "_" not in display:
        gameover=True
        print("Congratulations! You guessed the word correctly.")



        
