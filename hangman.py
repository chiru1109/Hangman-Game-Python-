import random
#Hangman Game
print("Welcome to Hangman Game.....")
Name = input("Enter Your Name: ")
print("Hello, " + Name + "Best of Luck!")
Rules = "1.Guess the word in Less than 6 wrong attempts \n2.You can guess the one letter at a time \n3.If you guess wrong more then 6 times the game ends"
print(Rules)
Min_Error = 0
Max_Error = 6
words = ["banana","apple","mango","grapes","watermelon","strawberry","orange"]
word = random.choice(words).lower()
Guess = ""
while Min_Error<Max_Error:
    guess = input("Guess the word: ").lower()
    Guess += guess
    Display_word=""
    for letter in word:
        if letter in Guess:
            Display_word += letter
        else:
            Display_word += "_"
    print(Display_word)
    if guess not in word:
        Min_Error += 1
        print("Wrong Guess",Max_Error-Min_Error,"Chances Left")
        
    if Display_word == word:
        won = True
        break
    if Display_word != word and Min_Error == Max_Error:
        won = False
        break
       
if won:
    print("Congratulations! You have guessed the word correctly.")
else:
    print("Sorry! You have run out of chances. The word was:", word)