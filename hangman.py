import word
import random

#importing and picking an external word.
word_list = word.word
random_word = word_list[random.randint(0,len(word_list)-1)]
random_word = "trumma"

#Constants
Guessed_letter = []
score = 0
winning_condition = 0
printed_word = ""

#Printing out the length of the word for first run. 
for i in random_word:
        printed_word = printed_word + " _ "
print(f"Guess the word: {printed_word}")
print(f"you have {4 -score } more try.")

while True:
    printed_word = ""
    
    letter = input("Give a letter: ").lower()
    if letter not in Guessed_letter:
            x = 0
            for i in random_word:
                if i == letter:
                    winning_condition += 1
                    x= 1

            if x > 0:
                 score -=1
            score += 1
            x = 0         
                
    Guessed_letter.append(letter)

    #Puts the 
    for i in random_word:
        if i in Guessed_letter:
            printed_word = printed_word + i
        else:
            printed_word = printed_word + " _ "

    #Winning or losing Conditions
    if winning_condition == len(random_word):
        print("You gussed the right word!")
        break
    if score > 3:
        print(f"You lost, you got the wrong letter {score} times")
        print(f"The right word was: {random_word}")
        break
    
    print(f"Guess the word: {printed_word}")
    print(f"You have guessed: {Guessed_letter}")
    print(f"You have gussed wrong {score} times, you have {4 -score } more try.")

