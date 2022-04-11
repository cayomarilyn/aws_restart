import random
print( "Welcome yo guess the number")
print( "the rules are simple. i will think of a number, and you will try to guess it.")
for x in range (0, 11):
      print(x)
isGuessRight = False
while isGuessRight != True:
     guess= input("Guess a number between 1 and 10: ")
     if int(guess) == x:
        print(" You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
     else:
        print(" You guessed {}. Sorry, that isn´t it. Try again".format(guess))
         
         
         